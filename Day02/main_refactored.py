with open("input.txt") as f:
    raw_in = "\n".join([line.strip() for line in f])

puz_in = raw_in.split("\n")

moves = {"X": 1, "Y": 2, "Z": 3}
wins = {"A Y", "B Z", "C X"}
ties = {"A X", "B Y", "C Z"}


def calc_score(match):
    move, your_move = match.split()
    move_score = moves[your_move]
    if match in wins:
        return move_score + 6
    elif match in ties:
        return move_score + 3
    return move_score


def calc_move(match):
    move, state = match.split()
    table = {
        "X": {
            "A": "Z",
            "B": "X",
            "C": "Y"
        },
        "Y": {
            "A": "X",
            "B": "Y",
            "C": "Z"
        },
        "Z": {
            "A": "Y",
            "B": "Z",
            "C": "X"
        }
    }
    return f"{move} {table[state][move]}"


print("Part 1:", sum([calc_score(match) for match in puz_in]))
print("Part 2:", sum([calc_score(calc_move(match)) for match in puz_in]))
