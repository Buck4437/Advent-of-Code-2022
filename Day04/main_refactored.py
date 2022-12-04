from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])
puz_in = s.split("\n")

vals = ints(puz_in, neg=False)

ct = 0
for s1, e1, s2, e2 in vals:
    if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
        ct += 1

t2 = 0
for s1, e1, s2, e2 in vals:
    if s1 <= e2 and s2 <= e1:
        t2 += 1

print("Part 1:", ct)
print("Part 2:", t2)
