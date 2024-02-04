#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################

import hangman_helper

FIRST_MESSAGE = '\nHave fun'
MESSAGE1 = "\nthe input is invalid try again"
MESSAGE2 = '\nyou already try this letter'
MESSAGE3 = '\nnice shot you found a letter'
MESSAGE4 = '\nthis letter is not in the wanted word'
MESSAGE5 = '\nthis is the wrong word'
MESSAGE6 = '\ndoes that help you'
MESSAGE7 = '\nGame Over,' \
           '\nyou had to find {}'
MESSAGE8 = '\nYou Won!!!'
MESSAGE9 = '\nyou have played {} games,yon won with {} points' \
           '\nDo you want play an other round?'
MESSAGE10 = '\nyou have played {} games' \
            '\ndo you want play a new game?'


def update_word_pattern(word, pattern, letter):
    """
    the function return the new pattern after we add to the pattern the letter just if  the letter is in the  word
    :param word: this is the word we looking for  looking for
    :param pattern: it'is like the word with holes and we have to complete those holes in order to find the word
    :param letter: we will check if the letter is in the word if yes we will add it in the pattern in the sames
    emplacements of this letter in the word
    :return: the function return the update pattern with the letter if the letter in the word
    """
    pattern_result = ''
    lst = [pattern[i] for i in range(len(pattern))]
    for j in range(len(word)):
        if word[j] == letter:
            lst[j] = letter
    for k in range(len(lst)):
        pattern_result += str(lst[k])
    return pattern_result


def remove_word(words_list, del_lst):
    """the function remove  a word of the words list if this word is in del_list
    :param del_lst: list of words that user choose
    :param words_list: list of words that the user insert
    """
    for i in del_lst:
        if i in words_list:
            words_list.remove(i)


def check_the_length(words_list, pattern):
    """
    the function remove the words of words list that aren't the same length of th pattern
    :param words_list: list of words
    :param pattern: the word we looking for with holes
    """
    del_list = []
    for k in words_list:
        if len(k) != len(pattern):
            del_list.append(k)
    remove_word(words_list, del_list)


def check_pattern_letters(words_list, pattern):
    """
    the function remove the words in the words_list that can't match with the pattern
    :param words_list: list of words
    :param pattern: the word we looking for with holes
    """
    del_list = []
    for i in words_list:
        for k in range(len(pattern)):
            if pattern[k] != "_" and pattern[k] != i[k]:
                del_list.append(i)
        for n in pattern:
            if n != '_':
                if pattern.count(n) != i.count(n):
                    del_list.append(i)

    remove_word(words_list, del_list)


def check_wrong_guess(words_list, wrong_guess_lst):
    """
    the function remove the words in words_list that contain a letter in the wrong_guess_list
    :param words_list: list of words
    :param wrong_guess_lst: list of letters
    """
    del_list = []
    for m in words_list:
        for letter in wrong_guess_lst:
            if letter in m:
                del_list.append(m)
    remove_word(words_list, del_list)


def filter_words_list(words_list, pattern, wrong_guess_lst):
    """
    the function return a list of words that can be the word that we looking for
    :param words_list: list of words
    :param pattern: the word we looking for with holes
    :param wrong_guess_lst: list of letters that aren't in th word that we looking for
    :return: list of word that can be the word that we looking for
    """
    check_the_length(words_list, pattern)
    check_wrong_guess(words_list, wrong_guess_lst)
    check_pattern_letters(words_list, pattern)
    return words_list


def list_of_hints(words_list, pattern, wrong_guess_lst):
    """
    Check how many elements there are in the list of hints and return the list of number of hints we wanted
    :param words_list: list of words
    :param pattern: the word we looking for with holes
    :param wrong_guess_lst: list of letters that aren't in th word that we looking for
    :return: the list of number of hints we wanted
    """
    HINT_LENGTH = hangman_helper.HINT_LENGTH
    lst_of_hints = filter_words_list(words_list, pattern, wrong_guess_lst)
    lst_of_hints2 = lst_of_hints[:]
    if len(lst_of_hints2) > HINT_LENGTH:
        lst_of_hints2 = []
        for i in range(HINT_LENGTH):
            emplacement = (i * (len(lst_of_hints))) // HINT_LENGTH
            lst_of_hints2.append(lst_of_hints[emplacement])
    return lst_of_hints2


def run_single_game(words_list, score):
    """
    the function  run just one game of hangman
    :param words_list: this is a list of word and from it the word we looking for will be choose
    :param score: it' the number of point the player will have in the star of the game
    :return: the score of the player in the end of the game
    """

    wrong_guess_lst = []
    random_word = hangman_helper.get_random_word(words_list)
    pattern = '_' * len(random_word)
    hint_lst = words_list[:]
    msg = FIRST_MESSAGE
    while score > 0 and pattern != random_word:

        hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
        input_type,input_content = hangman_helper.get_input()
        if input_type == hangman_helper.LETTER:  # if the user wants to guess a letter
            if len(input_content) != 1 or input_content.isalpha() == False or input_content.islower() == False:
                msg = MESSAGE1

            elif input_content in pattern or input_content in wrong_guess_lst:
                msg = MESSAGE2

            elif input_content in random_word:
                n = 0  # it will be the number of time the letter will appear in the update pattern
                score -= 1
                pattern = update_word_pattern(random_word, pattern,input_content)
                pattern_lst1 = [l for l in pattern]
                for j in range(len(pattern_lst1)):
                    if input_content == pattern_lst1[j]:
                        n += 1
                score = score + n * (n + 1) // 2
                msg = MESSAGE3
            elif input_content not in random_word:
                score = score - 1
                wrong_guess_lst.append(input_content)
                msg = MESSAGE4
        elif input_type == hangman_helper.WORD:  # if the user wants to guess a word
            m = 0  # it will be the number of time the letter will appear in the update pattern
            score -= 1
            pattern_list2 = [i for i in pattern]
            if input_content == random_word:
                pattern = random_word
                for k in range(len(pattern_list2)):
                    if '_' == pattern_list2[k]:
                        m += 1
                score += m * (m + 1) // 2
            msg = MESSAGE5

        elif input_type == hangman_helper.HINT:  # if the user wants a hints
            score -= 1
            hint_lst_short = list_of_hints(hint_lst, pattern, wrong_guess_lst)
            hangman_helper.show_suggestions(hint_lst_short)
            msg = MESSAGE6

    if score == 0:
        msg = MESSAGE7
        hangman_helper.display_state(pattern, wrong_guess_lst, score, msg.format(random_word))
    elif pattern == random_word:
        msg = MESSAGE8
        hangman_helper.display_state(random_word, wrong_guess_lst, score, msg)
    return score


def main():
    """
    the function run how many games that the user want if in the end of a game the user have a positive score, the user
    have the possibility to continue the game with his last score. if he loose the game the user can choose if he wants
    to play a new game or to stop playing"""
    games = True
    num_of_game = 0
    list_of_words = hangman_helper.load_words()
    score = hangman_helper.POINTS_INITIAL

    while games:
        score = run_single_game(list_of_words, score)
        num_of_game += 1
        if score > 0:
            games = hangman_helper.play_again(MESSAGE9.format(num_of_game,score))

        else:
            score = hangman_helper.POINTS_INITIAL
            games = hangman_helper.play_again(MESSAGE10.format(num_of_game))
            num_of_game = 0


if __name__ == '__main__':
    main()