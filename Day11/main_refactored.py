from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


class Monkey:

    monkeys = {}

    def __init__(self, lines):
        ints_list = ints(lines.split("\n"), neg=False)

        idx = ints_list[0][0]
        test_val = ints_list[3][0]
        true_idx = ints_list[4][0]
        false_idx = ints_list[5][0]

        self.items = ints_list[1]
        self.checker = lambda x: true_idx if x % test_val == 0 else false_idx
        self.tally = 0

        if "* old" in lines:
            self.op = lambda x: x ** 2
        elif "*" in lines:
            self.op = lambda x: x * ints_list[2][0]
        else:
            self.op = lambda x: x + ints_list[2][0]

        Monkey.monkeys[idx] = self

    def inspect(self):
        while len(self.items) != 0:
            item = self.op(self.items.pop(0)) // 3
            Monkey.monkeys[self.checker(item)].items.append(item)
            self.tally += 1


monkeys = [Monkey(line) for line in s.split("\n\n")]
for _ in range(20):
    for monkey in monkeys:
        monkey.inspect()

print(mul(sorted([m.tally for m in monkeys])[-2:]))


