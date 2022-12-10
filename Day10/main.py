from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

puz_in = s.split("\n")

x_val = 1
cycle = 1
cache = None
idx = 0
cum = 0
while idx < len(puz_in):
    if (cycle - 20) % 40 == 0:
        print(cycle, x_val)
        cum += cycle * x_val
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

