with open("input.txt") as f:
    string = "\n".join([line.strip() for line in f])
puz_in = string.split("\n")

t = 0
for item in puz_in:
    half = len(item) // 2
    ia, ib = set(item[:half]), set(item[half:])
    for i in (ia & ib):
        if i.lower() == i:
            t += ord(i) - ord("a") + 1
        else:
            t += ord(i) - ord("A") + 27

print("Part 1:", t)

temp = []
t2 = 0
for item in puz_in:
    temp += [set(item)]
    if len(temp) >= 3:
        a, b, c = temp
        for i in (a & b & c):
            if i.lower() == i:
                t2 += ord(i) - ord("a") + 1
            else:
                t2 += ord(i) - ord("A") + 27
        temp = []
print("Part 2:", t2)
