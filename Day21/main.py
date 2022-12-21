from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

result = {}



ops = [x.split(": ") for x in s.split("\n")]

while True:
    for name, val in ops:
        if val.isdecimal():
            result[name] = int(val)
        for c in "+-*/":
            if f" {c} " in val:
                left, right = val.split(f" {c} ")
                if left in result and right in result:
                    if c == "+":
                        ans = result[left] + result[right]

                    if c == "-":
                        ans = result[left] - result[right]

                    if c == "*":
                        ans = result[left] * result[right]

                    if c == "/":
                        ans = result[left] / result[right]

                    result[name] = ans
    if "root" in result:
        print(result["root"])
        break
