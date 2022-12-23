from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.replace("\n", "") for line in f])


vec_neighbours = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


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

rounds = 0
while True:
    rounds += 1
    proposed = {}
    repeated = set()
    all_pos = set()
    all_unmoved = True
    for elf in elves:
        for pos in vecs_add(vec_neighbours, elf):
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
                if position in all_pos:
                    repeated.add(position)
                else:
                    all_pos.add(position)
                all_unmoved = False
                break
        else:
            proposed[elf] = elf
    if all_unmoved:
        print("Answer:", rounds)
        break
    if rounds % 10 == 0:
        print(rounds)

    new_elves = set()
    for elf, new_pos in proposed.items():
        if new_pos not in repeated:
            new_elves.add(new_pos)
        else:
            new_elves.add(elf)
    elves = new_elves
    orders = orders[1:] + orders[0]
