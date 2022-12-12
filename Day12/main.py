from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

start, end = (0, 0), (0, 0)
low_elevations = []


grid = {}
for r, st in enumerate(s.split("\n")):
    for c, ch in enumerate(st):
        grid[(r, c)] = ch
        if ch == "S":
            start = r, c
        if ch == "E":
            end = r, c
        if ch == "a" or ch == "S":
            low_elevations += [(r, c)]


def get_neighbour(coor):
    x, y = coor
    return (x+1, y), (x-1, y), (x, y+1), (x, y-1)


def to_level(lv):
    if lv == "S":
        return ord("a")
    if lv == "E":
        return ord("z")
    return ord(lv)


def find(start, endings, reverse=False):
    queue = [start]
    visited = set(start)
    steps = 0
    while len(queue) > 0:
        new_queue = []
        for point in queue:
            if point in endings:
                return steps
            cur_lv = to_level(grid[point])
            for neigh in get_neighbour(point):
                if neigh not in grid or neigh in visited: continue
                difference = to_level(grid[neigh]) - cur_lv
                if (reverse and difference >= -1) or (not reverse and difference <= 1):
                    new_queue.append(neigh)
                    visited.add(neigh)
        queue = new_queue
        steps += 1
    return -1


print("Part 1:", find(start, [end]))
print("Part 2:", find(end, low_elevations, reverse=True))
