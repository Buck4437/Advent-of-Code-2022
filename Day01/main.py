puz_input = []
with open("input.txt") as f:
    for line in f:
        puz_input.append(line.strip())


def part1():
    m = 0
    t = 0
    for l in puz_input:
        if l.strip() == "":
            if t > m:
                m = t
            t = 0
        else:
            val = int(l)
            t += val
    return max(m, t)


def part2():
    vals = []
    t = 0
    for l in puz_input:
        if l.strip() == "":
            vals.append(t)
            t = 0
        else:
            val = int(l)
            t += val
    vals.append(t)
    return sum(sorted(vals)[-3:])


def main():
    print(part1())
    print(part2())


main()
