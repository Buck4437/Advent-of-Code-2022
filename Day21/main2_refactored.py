with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

jobs = dict([(x[:4], x[6:]) for x in s.split("\n")])
equations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}


def calc(name, humn):
    if name == "humn":
        return humn
    val = jobs[name]
    if val.isdecimal():
        return int(val)
    l, op, r = calc(val[:4], humn), val[5], calc(val[7:], humn)
    if name == "root":
        return l, r
    return equations[op](l, r)


def bin_search(upper):
    low, high = 0, upper
    while low <= high:
        mid = (low + high) // 2
        a, b = calc("root", humn=mid)
        if a == b:
            return mid
        if a > b:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def recurse_test(index, prev_num=0):
    for i in range(10):
        val = prev_num + 10 ** index * i
        a, b = calc("root", humn=val)
        deviance = b - a
        if deviance == 0:
            return val
        if deviance > 0:
            return recurse_test(index - 1, prev_num + 10 ** index * (i - 1))
    return recurse_test(index - 1, prev_num + 10 ** index * 9)


def recurse_test_binary(index, prev_num=0):
    val = prev_num + 2 ** index
    a, b = calc("root", humn=val)
    deviance = b - a
    if deviance == 0:
        return val
    if deviance > 0:
        return recurse_test_binary(index - 1, prev_num)
    return recurse_test_binary(index - 1, prev_num + 2 ** index)


print(bin_search(1e17))
print(recurse_test(index=15))
print(recurse_test_binary(index=60))
