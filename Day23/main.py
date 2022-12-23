from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.replace("\n", "") for line in f])


def get_neigh():
    neighs = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == y == 0:
                continue
            neighs.append((x, y))
    return neighs


# Mid is always the vector of movement
checks = {
    "N": [(-1, -1), (-1, 0), (-1, 1)],
    "S": [(1, -1), (1, 0), (1, 1)],
    "E": [(-1, 1), (0, 1), (1, 1)],
    "W": [(-1, -1), (0, -1), (1, -1)]
}


orders = "NSWE"
elves = set()


for r, row in enumerate(s.split("\n")):
    for c, char in enumerate(row):
        if char == "#":
            elves.add((r, c))

for _ in range(10):
    proposed = {}
    all_pos = []
    for elf in elves:
        for pos in vecs_add(get_neigh(), elf):
            if pos in elves:
                break
        # No elves
        else:
            proposed[elf] = elf
            continue
        # Hv elves
        for card in orders:
            for neigh in vecs_add(checks[card], elf):
                if neigh in elves:
                    break
            else:
                position = vec_add(checks[card][1], elf)
                proposed[elf] = position
                all_pos.append(position)
                break
        else:
            proposed[elf] = elf

    new_elves = set()
    repeated = [x for x in set(all_pos) if all_pos.count(x) > 1]
    for elf, new_pos in proposed.items():
        if new_pos not in repeated:
            new_elves.add(new_pos)
        else:
            new_elves.add(elf)
    elves = new_elves

    r_min, r_max = min([r for r, c in elves]), max([r for r, c in elves])
    c_min, c_max = min([c for r, c in elves]), max([c for r, c in elves])
    for i in range(r_min, r_max + 1):
        for j in range(c_min, c_max + 1):
            if (i, j) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

    orders = orders[1:] + orders[0]
    print(orders)

r_min, r_max = min([r for r, c in elves]), max([r for r, c in elves])
c_min, c_max = min([c for r, c in elves]), max([c for r, c in elves])

r_delta = r_max - r_min + 1
c_delta = c_max - c_min + 1
print(r_delta * c_delta - len(elves))