from aoc import *
import re

with open("test.txt") as f:
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

dir_to_vec = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

dir_to_score = "RDLU"


def turn_left(r, c):
    return -c, r


def turn_right(r, c):
    return c, -r


def wrap(next_cell, next_facing):
    direction = vec_to_dir[next_facing]
    if next_cell in grid:
        return next_cell, next_facing
    r, c = next_cell
    if r == -1 and direction == "U":
        if 50 <= c <= 99:
            return (c + 100, 0), dir_to_vec["R"]
        if 100 <= c <= 149:
            return (199, c - 100), dir_to_vec["U"]
    if 0 <= r <= 49:
        if c == 49 and direction == "L":
            return (149 - r, 0), dir_to_vec["R"]
        if c == 150 and direction == "R":
            return (149 - r, 99), dir_to_vec["L"]
    if r == 50:
        if 100 <= c <= 149 and direction == "D":
            return (c - 50, 99), dir_to_vec["L"]
    if 50 <= r <= 99:
        if c == 49 and direction == "L":
            return (100, r - 50), dir_to_vec["D"]
        if c == 100 and direction == "R":
            return (49, r + 50), dir_to_vec["U"]
    if r == 99:
        if 0 <= c <= 49 and direction == "U":
            return (c + 50, 50), dir_to_vec["R"]
    if 100 <= r <= 149:
        if c == -1 and direction == "L":
            return (149 - r, 50), dir_to_vec["R"]
        if c == 100 and direction == "R":
            return (149 - r, 149), dir_to_vec["L"]
    if r == 150:
        if 50 <= c <= 99 and direction == "D":
            return (c + 100, 49), dir_to_vec["L"]
    if 150 <= r <= 199:
        if c == -1 and direction == "L":
            return (0, r - 100), dir_to_vec["D"]
        if c == 50 and direction == "R":
            return (149, r - 100), dir_to_vec["U"]
    if r == 200:
        if 0 <= c <= 49 and direction == "D":
            return (0, c + 100), dir_to_vec["D"]
    print("Unhandled case:", next_cell, vec_to_dir[next_facing])


for i, step in enumerate(steps):
    new_pos, new_facing = cur, facing
    for _ in range(step):

        next_cell = vec_add(new_pos, new_facing)
        next_facing = new_facing
        next_cell, next_facing = wrap(next_cell, next_facing)
        if grid[next_cell] == "#":
            break
        new_pos = next_cell
        new_facing = next_facing

    cur = new_pos
    if i < len(turns):
        turn = turns[i]
        if turn == "L":
            facing = turn_left(*new_facing)
        else:
            facing = turn_right(*new_facing)

row, col, face = cur[0] + 1, cur[1] + 1, dir_to_score.index(vec_to_dir[facing])

print(row - 1, col - 1, vec_to_dir[facing])
print(row * 1000 + col * 4 + face)
