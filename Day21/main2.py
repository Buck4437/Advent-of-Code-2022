with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

ops = [x.split(": ") for x in s.split("\n")]


def test(i):
    result = {"humn": i}
    while True:
        new_ops = []
        for op in ops:
            name, val = op
            if name == "humn":
                continue
            if val.isdecimal():
                result[name] = int(val)
            elif name == "root":
                left, right = val.split(" + ")
                if left in result and right in result:
                    return result[left], result[right]
            else:
                for c in "+-*/":
                    if f" {c} " in val:
                        left, right = val.split(f" {c} ")
                        if left in result and right in result:
                            ans = None
                            if c == "+":
                                ans = result[left] + result[right]
                            if c == "-":
                                ans = result[left] - result[right]
                            if c == "*":
                                ans = result[left] * result[right]
                            if c == "/":
                                ans = result[left] / result[right]
                            result[name] = ans
            if name not in result:
                new_ops.append(op)


def recurse_test(indice, prev_num=0):
    for i in range(10):
        val = prev_num + 10 ** indice * i
        a, b = test(val)
        deviance = b - a
        print(val, a, b, deviance)
        if deviance == 0:
            return val
        if deviance > 0:
            return recurse_test(indice - 1, prev_num + 10 ** indice * (i - 1))
    return recurse_test(indice - 1, prev_num + 10 ** indice * 9)


def recurse_test_binary(indice, prev_num=0):
    val = prev_num + 2 ** indice
    a, b = test(val)
    deviance = b - a
    print(val, a, b, deviance)
    if deviance == 0:
        return val
    if deviance > 0:
        return recurse_test_binary(indice - 1, prev_num)
    return recurse_test_binary(indice - 1, prev_num + 2 ** indice)


print(recurse_test(indice=15))
print(recurse_test_binary(indice=60))