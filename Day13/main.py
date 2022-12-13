from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else 0 if left == right else -1

    lst_l = [left] if isinstance(left, int) else left
    lst_r = [right] if isinstance(right, int) else right

    for i in range(min(len(lst_l), len(lst_r))):
        sub_l, sub_r = lst_l[i], lst_r[i]
        result = compare(sub_l, sub_r)
        if result != 0:
            return result
    return compare(len(lst_l), len(lst_r))


pairs = s.split("\n\n")
tot = 0
for i, pair in enumerate(pairs):
    a, b = pair.split("\n")
    ap, bp = eval(a), eval(b)
    if compare(ap, bp) >= 0:
        tot += (i + 1)
print(tot)


packets = [eval(x) for x in s.split("\n") if x != ""]
a, b = [[2]], [[6]]
packets.extend([a, b])
sorted_packets = merge_sort(packets, compare)
print(mul([sorted_packets.index(x) + 1 for x in [a, b]]))
