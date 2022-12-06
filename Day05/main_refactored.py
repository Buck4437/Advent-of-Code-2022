from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])
puz_in = s.split("\n")

stacks_original = [
    None,
    "JHPMSFNV",
    "SRLMJDQ",
    "NQDHCSWB",
    "RSCL",
    "MVTPFB",
    "TRQNC",
    "GVR",
    "CZSPDLR",
    "DSJVGPBF"
]

vals = ints(puz_in, neg=False)
stacks_p1 = stacks_original.copy()
stacks_p2 = stacks_original.copy()

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
