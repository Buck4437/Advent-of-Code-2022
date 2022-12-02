with open("input.txt") as f:
    string = "\n".join([line.strip() for line in f])

puz_in = string.split("\n")

mp = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


wins = {"A Y", "B Z", "C X"}
sm = {"A X", "B Y", "C Z"}
tot = 0
for l in puz_in:
    tot += mp[l[2]]
    if l in wins:
        tot += 6
    elif l in sm:
        tot += 3

wins = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

sm = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

print("Part 1:", tot)
tot = 0
for l in puz_in:
    o, st = l[0], l[2]
    if st == "X":
        u = lose[o]
    elif st == "Y":
        u = sm[o]
        tot += 3
    elif st == "Z":
        u = wins[o]
        tot += 6
    else:
        print("No")
        u = "X"
    tot += mp[u]

print("Part 2:", tot)
