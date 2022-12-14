from aoc import *
from collections import defaultdict

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


def parse_coord(str_coord):
    return tuple(map(int, str_coord.split(",")))[::-1]


rocks = defaultdict(lambda: False)
# For visualization only
stationary_sand = defaultdict(lambda: False)
for path in s.split("\n"):
    sections = [parse_coord(x) for x in path.split(" -> ")]
    for i in range(len(sections) - 1):
        for rock in line(sections[i], sections[i+1]):
            rocks[rock] = True

floor = max([rock[0] for rock in rocks]) + 2


def has_block(pos):
    return rocks[pos]


sand_source = (0, 500)
moves = (1, 0), (1, -1), (1, 1)
count = 0
while True:
    if sand_source in rocks:
        break
    sand_pos = sand_source
    while True:
        if sand_pos[0] >= floor:
            break
        for pos in [vec_add(move, sand_pos) for move in moves]:
            if not has_block(pos):
                sand_pos = pos
                break
        else:
            break
    if sand_pos[0] >= floor:
        break
    rocks[sand_pos] = True
    stationary_sand[sand_pos] = True
    count += 1


print(count)


def lookup(r, c):
    if stationary_sand[(r, c)]:
        return "o"
    if (r, c) == (0, 500):
        return "+"
    if rocks[(r, c)]:
        return "#"
    return "."


min_c, max_c = min([rock[1] for rock in rocks]), max([rock[1] for rock in rocks])
for r in range(-1, floor):
    for c in range(min_c - 1, max_c + 2):
        print(lookup(r, c), end="")
    print()
