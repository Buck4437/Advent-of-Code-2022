from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


class Monkey:

    def __init__(self, monkey):
        val_list = ints(monkey.split("\n"), neg=False)
        self.idx, self.items = val_list[0][0], val_list[1]
        self.items = [int(worry) for worry in self.items]
        self.operand, self.tst, self.true, self.false = ints([monkey], neg=True)[0][-4:]
        self.inspects = 0
        Monkey.common_factor *= self.tst

        if "+" in monkey:
            self.op = "+"
        elif "* old" in monkey:
            self.op = "**"
        else:
            self.op = "*"

        Monkey.monkeys[self.idx] = self

    def receive(self, item):
        self.items.append(item)

    def inspect(self):
        while len(self.items) != 0:
            item = self.items.pop(0)
            if self.op == "+":
                item += self.operand
            elif self.op == "**":
                item **= 2
            else:
                item *= self.operand
            item %= Monkey.common_factor
            if item % self.tst == 0:
                Monkey.monkeys[self.true].receive(item)
            else:
                Monkey.monkeys[self.false].receive(item)
            self.inspects += 1

    monkeys = {}
    common_factor = 1


monkeys = [Monkey(line) for line in s.split("\n\n")]
for i in range(10000):
    for monkey in monkeys:
        monkey.inspect()

print(mul(sorted([monkey.inspects for monkey in monkeys])[::-1][:2]))
