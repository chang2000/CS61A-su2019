""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
# Q1
def lines_from_file(path):
    file = open(path)
    para_list = readlines(file)
    for i in range(len(para_list)):
        para_list[i] = strip(para_list[i],'\n ')
        # para_list[i] = para_list[i].rstrip()
    return para_list
def new_sample(path, i):
    return lines_from_file(path)[i]
# file = lines_from_file("./test.txt")
# print(file[0])
# print(len(file[0]))
# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________
        substitute_char = ______________
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
