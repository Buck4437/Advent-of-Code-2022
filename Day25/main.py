with open("input.txt") as f:
    s = "\n".join([line.replace("\n", "") for line in f])

puz_in = s.split("\n")

total = 0
for num in puz_in:
    tmp = 0
    for i, char in enumerate(num[::-1]):
        tmp += (5 ** i) * {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}[char]
    total += tmp

val = ""
while total > 0:
    remainder = total % 5
    if remainder >= 3:
        remainder -= 5
    val += {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}[remainder]
    total -= remainder
    total = total // 5
print(val[::-1])
