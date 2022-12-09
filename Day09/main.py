from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

visited = set()
tail = [0, 0]
body = [0, 0]


def touching(tail, body):
    for i in range(-1, 2):
        for j in range(-1, 2):
            pos = body[0] + i, body[1] + j
            if tuple(tail) == pos:
                return True
    return False


for line in s.split("\n"):
    dir = line[0]
    dst = int(line[2:])
    for i in range(dst):
        if dir == "U":
            body[1] = body[1] - 1
        if dir == "D":
            body[1] = body[1] + 1
        if dir == "L":
            body[0] = body[0] - 1
        if dir == "R":
            body[0] = body[0] + 1
        if not touching(tail, body):
            if dir == "U":
                tail = [body[0], body[1]+1]
            if dir == "D":
                tail = [body[0], body[1]-1]
            if dir == "L":
                tail = [body[0]+1, body[1]]
            if dir == "R":
                tail = [body[0]-1, body[1]]
        visited.add(tuple(tail))

print(len(visited))