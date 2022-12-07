with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

for i in range(len(s)):
    if len(set(s[i:i+4])) == 4:
        print("Part 1", i+4)
        break

for i in range(len(s)):
    if len(set(s[i:i+14])) == 14:
        print("Part 2", i+14)
        break
