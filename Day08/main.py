from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

puz_in = [[int(i) for i in x] for x in s.split("\n")]
visible = set()
for i in range(len(puz_in)):
    line = puz_in[i]
    tmp = -1
    for j in range(len(line)):
        tree = line[j]
        if tree > tmp:
            visible.add((i, j))
            tmp = tree
    tmp = -1
    for j in range(len(line)-1, -1, -1):
        tree = line[j]
        if tree > tmp:
            visible.add((i, j))
            tmp = tree

for i in range(len(puz_in)):
    tmp = -1
    for j in range(len(puz_in)):
        tree = puz_in[j][i]
        if tree > tmp:
            visible.add((j, i))
            tmp = tree
    tmp = -1
    for j in range(len(puz_in)-1, -1, -1):
        tree = puz_in[j][i]
        if tree > tmp:
            visible.add((j, i))
            tmp = tree

print(len(visible))
print(visible)