import re


def ints(lst, neg, lines=False):
    if lines:
        lst = lst.split("\n")
    nums = []
    for itm in lst:
        if neg:
            matches = re.findall("-?\d+", itm)
        else:
            matches = re.findall("\d+", itm)
        nums.append([int(s) for s in matches])
    return nums


def mul(lst):
    result = 1
    for x in lst:
        result *= x
    return result


def merge_sort(lst, comparator=None):
    L = lst[:]
    if comparator is None:
        def comparator(x, y):
            return 1 if x < y else 0 if x == y else -1
    if len(lst) <= 1:
        return L
    half = len(lst) // 2
    return __merge(merge_sort(L[:half], comparator), merge_sort(L[half:], comparator), comparator)


def __merge(l1, l2, comparator):
    lst = []
    while min(len(l1), len(l2)) > 0:
        a, b = l1[0], l2[0]
        if comparator(a, b) > -1:
            lst.append(l1.pop(0))
        else:
            lst.append(l2.pop(0))
    return lst + l1 + l2


def vec_add(v1, v2):
    return tuple([sum(x) for x in zip(v1, v2)])


def line(start, end):
    r1, c1 = start
    r2, c2 = end
    r_min, r_max = min(r1, r2), max(r1, r2)
    c_min, c_max = min(c1, c2), max(c1, c2)
    coords = []
    for r in range(r_min, r_max+1):
        for c in range(c_min, c_max+1):
            coords.append((r, c))
    return coords
