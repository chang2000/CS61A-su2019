"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    result = 1
    while k > 0:
        result = result * (n)
        k = k - 1
        n = n - 1
    return result


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    digits_list = []
    while n > 0:
        digits_list.append(n % 10)
        n = n // 10
    for i in range(len(digits_list) - 1):
        if digits_list[i] == 8 and digits_list[i + 1] == 8:
            return True
    return False

