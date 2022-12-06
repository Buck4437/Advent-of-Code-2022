from aoc import *

with open("input_parsing.txt") as f:
    s = "\n".join([line.strip() for line in f])

stacks_raw, moves = s.split("\n\n")

stacks_parsed = ["".join(x).strip() for x in zip(*[list(line[1::4]) for line in stacks_raw.split("\n")[:-1]][::-1])]
stacks_parsed.insert(0, "")

vals = ints(moves, neg=False, lines=True)
stacks_p1 = stacks_parsed.copy()
stacks_p2 = stacks_parsed.copy()

for n, st, end in vals:
    for i in range(n):
        itm = stacks_p1[st][-1]
        stacks_p1[st] = stacks_p1[st][:-1]
        stacks_p1[end] += itm
    itm = stacks_p2[st][-n:]
    stacks_p2[st] = stacks_p2[st][:-n]
    stacks_p2[end] += itm

print("".join([stacks_p1[i][-1] for i in range(1, len(stacks_p1))]))
print("".join([stacks_p2[i][-1] for i in range(1, len(stacks_p2))]))
