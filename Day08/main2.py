from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

puz_in = [[int(i) for i in x] for x in s.split("\n")]
best = 0
for i in range(len(puz_in)):
    for j in range(len(puz_in)):
        score = 1
        base = puz_in[i][j]
        tmp = 0
        for a in range(j+1, len(puz_in)):
            tree = puz_in[i][a]
            tmp += 1
            if tree >= base:
               break
        score *= tmp
        tmp = 0
        for a in range(j-1, -1, -1):
            tree = puz_in[i][a]
            tmp += 1
            if tree >= base:
               break
        score *= tmp
        tmp = 0
        for a in range(i+1, len(puz_in)):
            tree = puz_in[a][j]
            tmp += 1
            if tree >= base:
               break

        score *= tmp
        tmp = 0
        for a in range(i-1, -1, -1):
            tree = puz_in[a][j]
            tmp += 1
            if tree >= base:
               break
        score *= tmp
        best = max(score, best)
print(best)