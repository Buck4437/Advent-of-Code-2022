from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


class Item:

    def __init__(self, worry):
        self.worry = worry

    def __str__(self):
        return str(self.worry)


class Monkey:

    def __init__(self, monkey):
        ints_list = ints(monkey.split("\n"), neg=False)
        self.idx, self.items = ints_list[0][0], ints_list[1]
        self.items = [Item(int(worry)) for worry in self.items]
        self.operand, self.tst, self.true, self.false = ints([monkey], neg=True)[0][-4:]
        self.inspects = 0

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
                item.worry += self.operand
            elif self.op == "**":
                item.worry **= 2
            else:
                item.worry *= self.operand
            item.worry //= 3
            item.worry %= self.tst
            if item.worry % self.tst == 0:
                Monkey.monkeys[self.true].receive(item)
            else:
                Monkey.monkeys[self.false].receive(item)
            self.inspects += 1

    monkeys = {}


monkeys = [Monkey(line) for line in s.split("\n\n")]
for i in range(20):
    for monkey in monkeys:
        monkey.inspect()

print(mul(sorted([monkey.inspects for monkey in monkeys])[::-1][:2]))
