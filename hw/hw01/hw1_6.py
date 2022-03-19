def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    cnt = 0
    while x != 1:
        cnt += 1
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1
        print(x)
    return cnt


a = hailstone(27)
print(a)
