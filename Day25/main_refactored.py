with open("input.txt") as f:
    s = "\n".join([line.replace("\n", "") for line in f])

puz_in = s.split("\n")
table = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
reverse_table = dict([pair[::-1] for pair in table.items()])


def decode(snafu):
    tmp = 0
    for i, char in enumerate(snafu[::-1]):
        tmp += (5 ** i) * table[char]
    return tmp


def encode(deci):
    val = ""
    while deci > 0:
        remainder = deci % 5
        if remainder >= 3:
            remainder -= 5
        val += reverse_table[remainder]
        deci = (deci - remainder) // 5
    return val[::-1]


print(encode(sum(map(decode, puz_in))))