from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

puz_in = s.split("\n")
cycle = 1
x_val = 1
total = 0


def clock():
    global cycle, total
    trace()
    if (cycle - 20) % 40 == 0:
        total += cycle * x_val
    cycle += 1


def trace():
    column = ((cycle - 1) % 40)
    if abs(column - x_val) <= 1:
        print("█", end="")
    else:
        print(" ", end="")
    if cycle % 40 == 0:
        print()


def execute(line):
    global x_val
    if "noop" == line:
        clock()
    else:
        val = int(line[5:])
        clock()
        clock()
        x_val += val


for line in puz_in:
    execute(line)
# print(total)
