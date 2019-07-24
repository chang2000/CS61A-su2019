""" Lab 04 Optional Questions """

from lab04 import *

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    seq_mid = [x for x in s if round(sqrt(x)) ** 2 == x]
    seq_final = [int(sqrt(x)) for x in seq_mid]
    return seq_final

def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    "*** YOUR CODE HERE ***"
    return list (d.keys()) [list (d.values()).index (min(list(d.values())))]
    return min(d, key = lambda x: d[x])

