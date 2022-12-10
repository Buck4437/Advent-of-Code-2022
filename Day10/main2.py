from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

puz_in = s.split("\n")

x_val = 1
cycle = 1
cache = None
idx = 0
cum = 0
pixels = set()
while idx < len(puz_in):
    c = (cycle - 1) % 40
    if c in [x_val + i for i in [-1, 0, 1]]:
        print("#", end="")
    else:
        print(".", end="")
    if cycle % 40 == 0:
        print()

    line = puz_in[idx]
    if cache is not None:
        x_val += cache
        cache = None
        idx += 1
    elif "noop" in line:
        idx += 1
    else:
        delta = ints(line, neg=True, lines=True)[0][0]
        cache = delta
    cycle += 1
print(cum)

