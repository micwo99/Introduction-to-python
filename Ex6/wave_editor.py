import copy
from wave_helper import *
import math
from os.path import exists

BASIC_SAMPLE_RATE = 2000
MAX_VOLUME = 32767
MIN_VOLUME = -32768


def inverse_audio(input_list):
    """
    the function returns input list after having inverted it
    :param input_list: data_audio
    :return: the inverse of input_list
    """
    for i in range(int(len(input_list) / 2)):
        input_list[i], input_list[-i - 1] = \
            input_list[-i - 1], input_list[i]

    return input_list


def accelerate_audio_speed(lst):
    """
    the function returns a list  that corresponds to the data audio
    of the audio which has been accelerated by 2
    :param lst:data audio
    :return: list without all the items of lst that the
    index  in lst isn't a multiple of 2
    """
    new_lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            new_lst.append(lst[i])
    return new_lst


def decelerate_audio_speed(lst):
    """
    the function returns a list that corresponds to the data audio of
    the audio which was slowed down by 2
    :param lst: data audio
    :return: list that we add between each pair of samples,
    a pair of samples which is the average of these samples
    """
    new_lst = []
    for i in range(len(lst) - 1):
        new_lst.append(lst[i])
        a = int((lst[i][0] + lst[i + 1][0]) / 2)
        b = int((lst[i][1] + lst[i + 1][1]) / 2)
        new_lst.append([a, b])
    new_lst.append(lst[-1])
    return new_lst


def negative_sound(input_list):
    """
    the functions returns a list that correspond to the data audio of the audio
    which  is the input_list with their negative value
    :param input_list: data audio
    :return: list of input_list with its negative values
    """
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == MIN_VOLUME:
                input_list[i][j] = MAX_VOLUME
            else:
                input_list[i][j] = -1 * input_list[i][j]

    return input_list


def increase_volume(input_list):
    """
    the function return a list that corresponds to the data audio of
    the audio whose volume has been multiplied by 1.2
    :param input_list: data audio
    :return: input lst that all its values has been divided multiplied by 1.2
    """
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if int(input_list[i][j] * 1.2) > MAX_VOLUME:
                input_list[i][j] = MAX_VOLUME
            elif int(input_list[i][j] * 1.2) < MIN_VOLUME:
                input_list[i][j] = MIN_VOLUME
            else:
                input_list[i][j] = int(input_list[i][j] * 1.2)

    return input_list


def decrease_volume(input_list):
    """
    the function return a list that corresponds to the data audio of
    the audio whose volume has been divided by 1.2
    :param input_list: data audio
    :return: input lst that all its values has been divided by 1.2
    """
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            input_list[i][j] = int(input_list[i][j] / 1.2)

    return input_list


def dimming_filter(input_list):
    """This function is dimming the input list"""
    if len(input_list) == 1:
        return input_list

    max_idx = len(input_list) - 1
    new_list = copy.deepcopy(input_list)

    new_list[0][0] = int((input_list[0][0] + input_list[1][0]) / 2)
    new_list[0][1] = int((input_list[0][1] + input_list[1][1]) / 2)

    new_list[max_idx][0] = int(
        (input_list[max_idx][0] + input_list[max_idx - 1][0]) / 2)
    new_list[max_idx][1] = int(
        (input_list[max_idx][1] + input_list[max_idx - 1][1]) / 2)

    for i in range(1, len(input_list) - 1):
        new_list[i][0] = int(
            (input_list[i - 1][0] +
             input_list[i][0] + input_list[i + 1][0]) / 3)
        new_list[i][1] = int(
            (input_list[i - 1][1] +
             input_list[i][1] + input_list[i + 1][1]) / 3)

    return new_list


def audio_modifications(current_lst, sample_rate):
    """
    the function modifies current_lst according to the
    functions that we defined previously
    :param sample_rate:
    :param current_lst: data audio
    """
    while True:
        choose_1 = input("1. Invert the audio\n2. Negative audio"
                         "\n3. Accelerate audio speed\n"
                         "4. Decelerate audio speed"
                         "\n5. Increasing the volume\n"
                         "6. Decreasing  the volume"
                         "\n7. Dimming filter\n8. Exit menu\n")
        if choose_1 == "1":
            current_lst = inverse_audio(current_lst)
            print("The file audio has been reversed")
        elif choose_1 == "2":
            current_lst = negative_sound(current_lst)
            print("The file audio has beenturn to negative")
        elif choose_1 == "3":
            current_lst = accelerate_audio_speed(current_lst)
            print("The audio has been accelerated")
        elif choose_1 == "4":
            current_lst = decelerate_audio_speed(current_lst)
            print("The audio has been decelerated")
        elif choose_1 == "5":
            current_lst = increase_volume(current_lst)
            print("The volume has been increased")
        elif choose_1 == "6":
            current_lst = decrease_volume(current_lst)
            print("The volume has been decreased")
        elif choose_1 == "7":
            current_lst = dimming_filter(current_lst)
            print("The volume has been dimmed")
        elif choose_1 == "8":
            exit_menu(sample_rate, current_lst)
            break
        else:
            print("There is an error. Choose an integer1"
                  " from 1 to 8")


def exit_menu(sample_rate, audio_data):
    """
    the function will ask to the user the
    name of the file that he wants to save the audio
    :param sample_rate:
    :param audio_data:
    """
    name_file = input("Choose the name of the file :")
    save_wave(sample_rate, audio_data, name_file)


def sample_value(note, index):
    """
    the function return  the sample value according to note
    :param note: music note
    :param index: the emplacement of the sample
    :return:sample value
    """
    SAMPLE_RATE = 2000
    MAX_VOLUME = 32767
    if note == "A":
        FREQ_A = 440
        samples_per_cycle = SAMPLE_RATE / FREQ_A
        value = MAX_VOLUME * \
                math.sin(math.pi * 2 * (index / samples_per_cycle))
    if note == "B":
        FREQ_B = 494
        samples_per_cycle = SAMPLE_RATE / FREQ_B
        value = MAX_VOLUME * \
                math.sin(math.pi * 2 * (index / samples_per_cycle))
    if note == "C":
        FREQ_C = 523
        samples_per_cycle = SAMPLE_RATE / FREQ_C
        value = MAX_VOLUME * \
                math.sin(math.pi * 2 * (index / samples_per_cycle))
    if note == "D":
        FREQ_D = 587
        samples_per_cycle = SAMPLE_RATE / FREQ_D
        value = MAX_VOLUME * \
                math.sin(math.pi * 2 * (index / samples_per_cycle))
    if note == "E":
        FREQ_E = 659
        samples_per_cycle = SAMPLE_RATE / FREQ_E
        value = MAX_VOLUME * \
                math.sin(math.pi * 2 * (index / samples_per_cycle))
    if note == "F":
        FREQ_F = 698
        samples_per_cycle = SAMPLE_RATE / FREQ_F
        value = MAX_VOLUME * \
                math.sin(math.pi * 2 * (index / samples_per_cycle))
    if note == "G":
        FREQ_G = 784
        samples_per_cycle = SAMPLE_RATE / FREQ_G
        value = MAX_VOLUME * \
                math.sin(math.pi * 2 * (index / samples_per_cycle))
    if note == 'Q':
        value = 0

    return value


def composing_melody():
    """
    the function return list that corresponds to a data audio
    according to a directive file that we will check. if the file
    that the user is not valid the program
    will ask to the user to choose an other file until this file is valid
    :return: data audio
    """
    new_lst = []
    a = False
    while a == False:
        directive_file = input('choose a directive melody file:')
        if exists(directive_file) == False:
            print("The file doesn't exist")
            a = False
        else:
            a = True

    f = open(directive_file, 'r')
    all_f = f.read()
    f.close()
    lst = all_f.split()
    for n in range(len(lst)):
        if lst[n].isnumeric():
            lst[n] = int(lst[n])

    for i in range(0, len(lst) - 1, 2):
        for k in range(lst[i + 1] * 125):
            m = int(sample_value(lst[i], k))
            new_lst.append([m, m])

    return new_lst


def main_function():
    """
    the function asks to the user if he wants to modify a wav file or
    composing a melody
    and it allows to save the new wav file
    """
    while True:

        initial_choose = input(
            "1. Modifications on a wav file\n2. Tune composition\n3. Exit\n")

        if initial_choose == "1":
            while True:
                wave_filename = input("The name of the wav file :")
                loaded_result = load_wave(wave_filename)
                if loaded_result != -1:
                    sample_rate, current_lst = load_wave(wave_filename)
                    break
                else:
                    print("There is an error. "
                          "The file is not valid or does not exist")

            audio_modifications(current_lst, sample_rate)

        elif initial_choose == "2":
            current_lst = composing_melody()
            audio_modifications(current_lst, BASIC_SAMPLE_RATE)

        elif initial_choose == "3":
            break

        else:
            print("There is an error. Choose or 1 or 2 or 3")


if __name__ == '__main__':
    main_function()
