from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


nums = []
zero = None
for i, line in enumerate(s.split("\n")):
    pair = (int(line) * 811589153, i)
    if pair[0] == 0:
        zero = pair
    nums.append(pair)

lst = nums.copy()

for _ in range(10):
    for tuple in nums:
        change = tuple[0]
        position = lst.index(tuple)
        lst.pop(position)
        # Previous number
        prev_pos = (position - 1) % len(lst)
        new_position = (prev_pos + change) % len(lst)
        lst.insert(new_position + 1, tuple)


print(lst)
zero_pos = lst.index(zero)
sm = 0
for i in [1000, 2000, 3000]:
    pos = (zero_pos + i) % len(lst)
    print(lst[pos][0])
    sm += lst[pos][0]

print(sm)