with open("input.txt") as f:
    string = "\n".join([line.strip() for line in f])
puz_in = string.split("\n")


def get_priority(char):
    if char.lower() == char:
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


t = 0
for item in puz_in:
    half = len(item) // 2
    ia, ib = set(item[:half]), set(item[half:])
    for i in (ia & ib):
        t += get_priority(i)
print("Part 1:", t)

t2 = 0
temp = []
for item in puz_in:
    temp += [set(item)]
    if len(temp) >= 3:
        a, b, c = temp
        for i in (a & b & c):
            t2 += get_priority(i)
        temp = []
print("Part 2:", t2)
