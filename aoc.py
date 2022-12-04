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
