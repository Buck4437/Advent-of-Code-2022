from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

cubes = [tuple(x) for x in ints(s, True, True)]

min_ord, max_ord = min([min(*x) for x in cubes]), max([max(*x) for x in cubes])

c = 0
neighs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
air_pockets = set()
outer_air = set()
for cube in cubes:
    for cube_neighbour in vecs_add(neighs, cube):
        if tuple(cube_neighbour) in air_pockets or tuple(cube_neighbour) in outer_air:
            continue
        if tuple(cube_neighbour) in cubes:
            c += 1
        else:
            Q = [cube_neighbour]
            visited = {cube_neighbour}
            is_outer, is_inner = False, False
            while len(Q) > 0 and not is_outer and not is_inner:
                n_q = []
                for air in Q:
                    for air_neighbour in vecs_add(neighs, air):
                        if air_neighbour in air_pockets:
                            is_inner = True
                        if air_neighbour in outer_air or any([x < min_ord - 2 or x > max_ord + 2 for x in air_neighbour]):
                            is_outer = True
                        if tuple(air_neighbour) not in cubes and tuple(air_neighbour) not in visited:
                            n_q.append(air_neighbour)
                            visited.add(air_neighbour)
                Q = n_q
            if len(Q) == 0 or is_inner:
                for v in visited:
                    air_pockets.add(v)
            else:
                for v in visited:
                    outer_air.add(v)

d = 0
for pock in air_pockets:
    for cube_neighbour in vecs_add(neighs, pock):
        if tuple(cube_neighbour) in air_pockets:
            d += 1

print(len(cubes) * 6 - c - len(air_pockets) * 6 + d)
