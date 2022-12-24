from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.replace("\n", "") for line in f])

puz_in = s.split("\n")

blizzards_og = {
    "U": set(),
    "D": set(),
    "L": set(),
    "R": set()
}

grid = {}
arrow_to_dir = {"^": "U", "v": "D", "<": "L", ">": "R"}
dir_to_vec = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def wrap(r, c):
    r_min, r_max = 1, len(puz_in) - 2
    c_min, c_max = 1, len(puz_in[0]) - 2
    if r_min <= r <= r_max and c_min <= c <= c_max:
        return r, c
    if r < r_min:
        return r_max, c
    if r > r_max:
        return r_min, c
    if c < c_min:
        return r, c_max
    if c > c_max:
        return r, c_min


start, end = None, None
for r, row in enumerate(puz_in):
    for c, char in enumerate(row):
        if r == 0 and char == ".":
            start = (r, c)
        if r == len(puz_in) - 1 and char == ".":
            end = (r, c)
        if char in arrow_to_dir:
            blizzards_og[arrow_to_dir[char]].add((r, c))
        grid[(r, c)] = char


def get_new_blizzards(blizzards):
    new_blizzards = {}
    for direction in blizzards:
        vec = dir_to_vec[direction]
        blizs = set()
        for bliz in blizzards[direction]:
            new_bliz = wrap(*vec_add(bliz, vec))
            blizs.add(new_bliz)
        new_blizzards[direction] = blizs
    return new_blizzards


def find_min(elapsed, starting_pos, ending_pos):
    blizzards = blizzards_og.copy()
    for _ in range(elapsed):
        blizzards = get_new_blizzards(blizzards)

    elapsed = 0
    positions = {starting_pos}
    while len(positions) > 0:
        # Simulate move
        blizzards = get_new_blizzards(blizzards)

        new_positions = set()
        for position in positions:
            if position == ending_pos:
                return elapsed
            for neigh in vecs_add([(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)], position):
                if neigh not in grid or grid[neigh] == "#":
                    continue
                for blizs in blizzards.values():
                    if neigh in blizs:
                        break
                else:
                    new_positions.add(neigh)
        positions = new_positions
        elapsed += 1
    return -1


p1 = find_min(0, start, end)
p2 = find_min(p1, end, start)
p3 = find_min(p1 + p2, start, end)
print(p1)
print(p1, p2, p3, p1 + p2 + p3)

