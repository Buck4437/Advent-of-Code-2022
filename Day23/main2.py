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

round = 0
while True:
    round += 1
    proposed = {}
    all_pos = []
    all_unmoved = True
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
                all_unmoved = False
                break
        else:
            proposed[elf] = elf
    if all_unmoved:
        print("Answer:", round)
        break
    if round % 10 == 0:
        print(round)

    new_elves = set()
    repeated = [x for x in set(all_pos) if all_pos.count(x) > 1]
    for elf, new_pos in proposed.items():
        if new_pos not in repeated:
            new_elves.add(new_pos)
        else:
            new_elves.add(elf)
    elves = new_elves
    orders = orders[1:] + orders[0]


