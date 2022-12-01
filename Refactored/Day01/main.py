with open("input.txt") as f:
    string = "\n".join([line.strip() for line in f])

vals = []
for block in string.split("\n\n"):
    num = sum([int(s) for s in block.split("\n")])
    vals.append(num)

print("Part 1:", max(vals))
print("Part 2:", sum(sorted(vals)[-3:]))
