from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])
puz_in = s.split("\n")

stacks = [
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

for n, st, end in vals:
    for i in range(n):
        itm = stacks[st][-1]
        stacks[st] = stacks[st][:-1]
        stacks[end] += itm

for i in range(1, len(stacks)):
    print(stacks[i][-1], end="")
print()


stacks = [
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

for n, st, end in vals:
    x = -n
    itm = stacks[st][x:]
    stacks[st] = stacks[st][:x]
    stacks[end] += itm

for i in range(1, len(stacks)):
    print(stacks[i][-1], end="")
print()
