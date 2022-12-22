from aoc import *
import re

with open("input.txt") as f:
    s = "\n".join([line.replace("\n", "") for line in f])

raw_map, raw_path = s.split("\n\n")
grid = {}
row_min, row_max = {}, {}
col_min, col_max = {}, {}
start = None

for r, row in enumerate(raw_map.split("\n")):
    for c, char in enumerate(row):
        if char != " ":
            grid[(r, c)] = char
        if start is None:
            start = (r, c)

steps = ints([raw_path.strip()], neg=False)[0]
turns = re.findall("[LR]", raw_path)
cur = start
facing = (0, 1)
vec_to_dir = {
    (0, 1): "R",
    (0, -1): "L",
    (1, 0): "D",
    (-1, 0): "U"
}
dir_to_score = "RDLU"


def turn_left(r, c):
    return -c, r


def turn_right(r, c):
    return c, -r


for i, step in enumerate(steps):
    new_pos = cur
    for _ in range(step):
        next_cell = vec_add(new_pos, facing)
        if next_cell not in grid:
            direction = vec_to_dir[facing]
            if direction == "R":
                next_cell = cur[0], min([c for r, c in grid if r == cur[0]])
            elif direction == "L":
                next_cell = cur[0], max([c for r, c in grid if r == cur[0]])
            elif direction == "D":
                next_cell = min([r for r, c in grid if c == cur[1]]), cur[1]
            elif direction == "U":
                next_cell = max([r for r, c in grid if c == cur[1]]), cur[1]
            else:
                print("WTF")
        if grid[next_cell] == "#":
            break
        new_pos = next_cell
    cur = new_pos
    if i < len(turns):
        turn = turns[i]
        if turn == "L":
            facing = turn_left(*facing)
        else:
            facing = turn_right(*facing)

row, col, face = cur[0] + 1, cur[1] + 1, dir_to_score.index(vec_to_dir[facing])

print(row * 1000 + col * 4 + face)
