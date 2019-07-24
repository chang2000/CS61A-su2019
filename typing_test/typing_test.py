""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
# Q1
def lines_from_file(path):
    file = open(path)
    para_list = readlines(file)
    # print(para_list)

    for i in range( len(para_list) ):
        para_list[i] = strip(para_list[i])
        # print(para_list[i])
        # para_list[i] = para_list[i].rstrip()
    # print(para_list)
    return para_list

def new_sample(path, i):
    return lines_from_file(path)[i]
# file = lines_from_file("./test.txt")
# print(file[0])
# print(len(file[0]))

def analyze(sample_paragraph, typed_string, start_time, end_time):

    def type_speed(string, start_time, end_time):
        word_list = split(string, None)
        type_length = len(string)
        return (60 * len(string)) / ((end_time - start_time) * 5)

    def type_accuracy(sample_paragraph, typed_string):
        # pre-process the strings
        typed_string = strip(typed_string)
        sample_list = split(sample_paragraph)
        typed_list = split(typed_string)
        if len(typed_list) == 0:
            return 0.0

        if len(sample_list) <= len(typed_list):
            counter = 0
            for i in range(len(sample_list)):
                if sample_list[i] == typed_list[i]:
                    counter += 1
            return counter * 100/ len(sample_list)

        elif len(sample_list) > len(typed_list):
            counter = 0
            for i in range(len(typed_list)):
                if sample_list[i] == typed_list[i]:
                    counter += 1
            return counter * 100/ len(typed_list)

    return [type_speed(typed_string, start_time, end_time), type_accuracy(sample_paragraph, typed_string)]

# q3
def pig_latin(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if word[0] in vowels:
        return word + "way"
    else:
        cluster = ""
        counter = 0
        for i in range(len(word)):
            if word[i] in vowels:
                counter = i
                break
            cluster = cluster + word[i]

    # word = word[i:]
    if counter == 0:
        return word + "ay"
    return str(word[counter:]) + cluster + "ay"

# q4
def autocorrect(user_input, word_list, score_function):
    if user_input in word_list:
        return user_input
    else:
        return min(word_list, key=lambda x: score_function(user_input, x))

# q5
def swap_score(str1, str2):
    if len(str1) == 0 and len(str2) >= 0:
        return 0
    elif len(str1) >= 0 and len(str2) == 0:
        return 0

    if str1[0] == str2[0]:
        return swap_score(str1[1:], str2[1:])
    else:
        return swap_score(str1[1:], str2[1:]) + 1


# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == word2:
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return 0
        # END Q6
    elif len(word1)== 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)

    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return score_function(word1[1:], word2[1:])
        # END Q6
    else:
        add_char = score_function(word1, word2[1:]) + 1 # Fill in these lines
        remove_char = score_function(word1[1:], word2) + 1
        substitute_char = score_function(word1[1:], word2[1:]) + 1
        # BEGIN Q6
        return min(add_char, remove_char, substitute_char)
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1, word2):
    if word1 == word2:
        return 0
    elif len(word1)== 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)

    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        return score_function_accurate(word1[1:], word2[1:])
    else:
        add_char = score_function_accurate(word1, word2[1:]) + 1 # Fill in these lines
        remove_char = score_function_accurate(word1[1:], word2) + 1

        factor = KEY_DISTANCES[(word1[0], word2[0])]

        substitute_char = score_function_accurate(word1[1:], word2[1:]) + factor

        return min(add_char, remove_char, substitute_char)


def score_function_final(word1, word2):
    word_score_dict = {}

    def helper(word1, word2):
        nonlocal word_score_dict
        if word1 == word2:
            return 0
        elif len(word1)== 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)

        if (word1, word2) in word_score_dict:
            return word_score_dict[(word1, word2)]

        elif (word2, word1) in word_score_dict:
            return word_score_dict[(word2, word1)]

        elif word1[0] == word2[0]:
            return helper(word1[1:], word2[1:])

        else:
            add_char = helper(word1, word2[1:]) + 1
            remove_char = helper(word1[1:], word2) + 1
            factor = KEY_DISTANCES[(word1[0], word2[0])]
            substitute_char = helper(word1[1:], word2[1:]) + factor

            score = min(add_char, remove_char, substitute_char)

            word_score_dict[(word1, word2)] = score
            # print(word_score_dict)
            return score
    return helper(word1, word2)
# END Q7-8

