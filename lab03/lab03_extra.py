""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    if n == 2:
        return True

    def helper(n,divider):
        if divider == 1:
            return True
        if n % divider == 0:
            return False
        return helper(n, divider - 1)

    return helper(n,n-1)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"

    def helper(n,digit):
        if n < 10:
            return 0
        elif n % 10 == digit:
            return helper(n,digit) + 1
        else:
            return helper(n,digit)
    return ten_pairs(n // 10) + helper(n // 10, 10 - n % 10)
