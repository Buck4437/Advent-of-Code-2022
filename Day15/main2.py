from aoc import *
import time

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

int_in = ints(s, neg=True, lines=True)

segments = []


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


scanners = []
distances = []

for x1, y1, bx, by in int_in:
    distances.append(manhattan(x1, y1, bx, by))
    scanners.append((x1, y1))


def main(boundary):
    for i, scanner in enumerate(scanners):
        dst = distances[i] + 1
        pos_vel = [
            [(0, -dst), (1, 1)],
            [(dst, 0), (-1, 1)],
            [(0, dst), (-1, -1)],
            [(-dst, 0), (1, -1)]
        ]
        print("Beacon", i + 1)
        for offset, vel in pos_vel:
            pos = vec_add(offset, scanner)
            shifts = 0
            while shifts < dst:
                if min(pos) < 0:
                    next_shift = abs(min(pos))
                elif max(pos) > boundary:
                    next_shift = abs(max(pos) - boundary)
                else:
                    for j, scanner2 in enumerate(scanners):
                        if scanner == scanner2:
                            continue
                        dst_from_scan = manhattan(*pos, *scanner2)
                        if dst_from_scan <= distances[j]:
                            next_shift = max((distances[j] - dst_from_scan) // 2, 1)
                            break
                    else:
                        print(pos)
                        print(pos[0] * 4000000 + pos[1])
                        return
                pos = vec_add(pos, vec_mul(vel, next_shift))
                shifts += next_shift


# boundary = int(input("Enter boundary: "))
boundary = 4000000
t0 = time.time()
main(boundary)
print(time.time() - t0)
