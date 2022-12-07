from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])
puz_in = s.split("\n")

dirs = {}
stack = []

for line in puz_in:
    if "$ cd" in line:
        if ".." in line:
            stack.pop()
        elif "/" in line:
            stack = []
        else:
            stack.append(line[5:])
    elif "$ ls" in line or "dir" in line:
        continue
    else:
        # item
        cur = dirs
        for item in stack:
            if item not in cur:
                cur[item] = {}
            cur = cur[item]
        size, name = line.split()
        if name not in cur:
            cur[name] = int(size)

print(dirs)


def calc_tot_size(rt: dict):
    tot = 0
    for key, val in rt.items():
        if isinstance(val, dict):
            tot += calc_tot_size(val)
        else:
            tot += val
    return tot


def find_dirs(rt: dict):
    dirs = tuple()
    for key, val in rt.items():
        if isinstance(val, dict):
            dirs += (calc_tot_size(val), )
            dirs += find_dirs(val)
    return dirs


print(sum([x for x in find_dirs(dirs) if x <= 100000]))
print(len([x for x in find_dirs(dirs) if x <= 100000]))

cur_ext = 70000000 - calc_tot_size(dirs)
needed = 30000000 - cur_ext
print(min([x for x in find_dirs(dirs) if x >= needed]))
