with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])
puz_in = s.split("\n")

ct = 0
for line in puz_in:
    p1, p2 = line.split(",")
    s1, e1 = [int(x) for x in p1.split("-")]
    s2, e2 = [int(x) for x in p2.split("-")]
    if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
        ct += 1

t2 = 0
for line in puz_in:
    p1, p2 = line.split(",")
    s1, e1 = [int(x) for x in p1.split("-")]
    s2, e2 = [int(x) for x in p2.split("-")]
    if not e1 < s2 and not e2 < s1:
        t2 += 1

print("Part 1:", ct)
print("Part 2:", t2)
