#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################


import itertools
from collections import Counter


class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose(self, symptoms):
        """
        the function receive symptoms and return the illness depending to the symptoms
        :param symptoms: list of symptoms
        :return: illness
        """
        return self.diagnose_helper(symptoms, self.root)

    def diagnose_helper(self, symptoms, root):
        if root.positive_child is None and root.negative_child is None:
            return root.data

        if root.data in symptoms:
            return self.diagnose_helper(symptoms, root.positive_child)
        else:
            return self.diagnose_helper(symptoms, root.negative_child)

    def calculate_success_rate(self, records):
        """
        the function calculs the success rate of the function diagnose depending to several record
        :param records: objects that contains the name of a illness and the symptoms of this illness
        :return: success rate
        """
        success = 0
        for record in records:
            if self.diagnose(record.symptoms) == record.illness:
                success += 1
        return success / len(records)

    def all_illnesses(self):
        """
        the function return the illnesses that appear in the leaves of the tree
        :return: list of illnesses
        """
        illness_dict = self.all_illnesses_helper(self.root, {})
        sorted_list = sorted(illness_dict, key=illness_dict.get, reverse=True)
        return sorted_list

    def all_illnesses_helper(self, node, illness_dict):

        if node is not None:
            if node.negative_child is None and node.positive_child is None:
                if node.data in illness_dict:
                    illness_dict[node.data] += 1
                    return illness_dict
                else:
                    illness_dict[node.data] = 1
                    return illness_dict
            self.all_illnesses_helper(node.positive_child, illness_dict)
            self.all_illnesses_helper(node.negative_child, illness_dict)
        return illness_dict

    def paths_to_illness(self, illness):
        """
        the function returns the different ways in which the tree arrives at a leave that is the parameters illness
         that the function receives
        :param illness: string
        :return:list of list
        """
        lst = []
        self.paths_to_illness_helper(illness, self.root, lst, [])
        return lst

    def paths_to_illness_helper(self, illness, node, list, result):

        if node is not None:
            if node.negative_child is None and node.positive_child is None:
                if node.data == illness:
                    list.append(result)
                return
            self.paths_to_illness_helper(illness, node.positive_child, list, result + [True])
            self.paths_to_illness_helper(illness, node.negative_child, list, result + [False])


def build_tree(records, symptoms):
    """
    the function return the root of the tree
    :param records: list of record objects
    :param symptoms: list of symptoms
    :return: root of the tree that the function built
    """
    return build_tree_helper(symptoms, records, [], [])


def build_tree_helper(symptoms, records, list1, list_symp):
    matched_record = []
    if symptoms == []:
        for record in records:
            if check_record_symptoms(record, list_symp, list1):
                matched_record.append(record.illness)
        if matched_record == []:
            return Node(None, None, None)
        else:
            final_leaf = Counter(matched_record).most_common()[0][0]
            return Node(final_leaf, None, None)
    else:
        root = Node(symptoms[0], build_tree_helper(symptoms[1:], records, list1 + [True], list_symp + [symptoms[0]]),
                    build_tree_helper(symptoms[1:], records, list1 + [False], list_symp + [symptoms[0]]))
        return root


def check_record_symptoms(record, symptoms, list):
    """
    the function create a list that contains booleans values and check if it the same as list

    :param record: record objects
    :param symptoms: list of symptoms
    :param list: list that contains booleans values
    :return:True/False
    """
    result = []
    symptoms_record = record.symptoms
    for symptom in symptoms:
        if symptom in symptoms_record:
            result.append(True)
        else:
            result.append(False)
    if list == result:
        return True


def optimal_tree(records, symptoms, depth):
    """
    the function builds trees whose length of these trees is equal to the parameter depth
    (using the function build_tree) and also hte function check the succes rate of each tree that it built with
    the precedent function. the function return the tree with the highest sucess rate
    :param records: list of record objects
    :param symptoms: list of symptoms
    :param depth: intergers
    :return: tree with the highest sucess rate
    """
    all_groups = itertools.combinations(symptoms, depth)

    all_trees = []
    max = -1
    max_t = None
    for x in all_groups:
        sub_tree = build_tree(records, list(x))
        dignsr = Diagnoser(sub_tree)
        succ_rate_tree = dignsr.calculate_success_rate(records)
        all_trees.append((sub_tree, succ_rate_tree))
    for group in all_trees:
        if group[1] > max:
            max = group[1]
            max_t = group[0]
    return max_t


if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

# Add more tests for sections 2-7 here.
