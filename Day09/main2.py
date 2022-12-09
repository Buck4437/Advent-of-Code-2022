with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


def touching(tail, body):
    for i in range(-1, 2):
        for j in range(-1, 2):
            pos = body[0] + i, body[1] + j
            if tuple(tail) == pos:
                return True
    return False


def dstce(tail, body):
    return abs(body[0] - tail[0]) + abs(body[1] - tail[1])


def sum_vec(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


visited = set()
chain = [(0, 0)] * 10


orthogonal = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}

diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


for line in s.split("\n"):
    direction = line[0]
    dst = int(line[2:])
    for x in range(dst):
        chain[0] = sum_vec(chain[0], orthogonal[direction])
        for i in range(1, 10):
            head, tail = chain[i-1], chain[i]
            if not touching(tail, head):
                list_of_moves = orthogonal.values() if dstce(tail, head) == 2 else diagonals
                for move in list_of_moves:
                    new_tail = sum_vec(tail, move)
                    if touching(new_tail, head):
                        chain[i] = new_tail
                        break
        visited.add(tuple(chain[-1]))

print(len(visited))

