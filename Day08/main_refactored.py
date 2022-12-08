from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

puz_in = [[int(i) for i in x] for x in s.split("\n")]
size = len(puz_in)
cache = {}


def get_line_of_sights(i, j):
    key = i, j
    if key in cache:
        return cache[key]
    left, right = puz_in[i][:j][::-1], puz_in[i][j+1:]

    cols = list(zip(*puz_in))
    top, bottom = list(cols[j][:i][::-1]), list(cols[j][i+1:])

    dirs = left, right, top, bottom
    cache[key] = dirs
    return dirs


def is_visible(i, j):
    tree = puz_in[i][j]
    dirs = get_line_of_sights(i, j)
    return any([all(x < tree for x in los) for los in dirs])


def count_trees(trees, base):
    cnt = 0
    for tree in trees:
        cnt += 1
        if tree >= base:
            break
    return cnt


def score(i, j):
    tree = puz_in[i][j]
    dirs = get_line_of_sights(i, j)
    return mul([count_trees(d, tree) for d in dirs])


count = 0
max_score = 0
for i in range(size):
    for j in range(size):
        if is_visible(i, j):
            count += 1
        max_score = max(max_score, score(i, j))
print("Part 1:", count)
print("Part 2:", max_score)
