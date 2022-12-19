from aoc import *

with open("input2.txt") as f:
    s = "\n".join([line.strip() for line in f])

datas = ints(s, False, True)


def maximize(datas, inv, robots, time, banned_bot=None):

    if banned_bot is None:
        banned_bot = set()

    idx, ore, clay, obs1, obs2, geode1, geode2 = datas

    new_inv = inv.copy()
    new_robots = robots.copy()

    if time <= 0:
        return new_inv["geode"]

    if time == 1:
        return new_inv["geode"] + new_robots["geode"]

    if time >= 28:
        print(time)

    # Too many robots = bad
    if new_robots["ore"] > max([ore, clay, obs1, geode1]):
        return 0
    
    if new_robots["clay"] > obs2:
        return 0

    recipes = {
        "geode": {
            "ore": geode1,
            "obsidian": geode2
        },
        "obsidian": {
            "ore": obs1,
            "clay": obs2
        },
        "clay": {
            "ore": clay
        },
        "ore": {
            "ore": ore
        }
    }

    can_be_produced = []
    results = [0]

    for robot_type, inputs in recipes.items():
        if robot_type == "ore":
            if new_robots["ore"] >= max([ore, clay, obs1, geode1]):
                continue
        if robot_type == "clay":
            if new_robots["clay"] >= obs2:
                continue
        clone_inv, clone_robots = new_inv.copy(), new_robots.copy()
        for ingredient, amount in inputs.items():
            if clone_inv[ingredient] < amount:
                break
        else:
            can_be_produced.append(robot_type)

    for key, value in robots.items():
        new_inv[key] += value

    for robot_type in can_be_produced:
        if robot_type in banned_bot:
            continue
        clone_inv, clone_robots = new_inv.copy(), new_robots.copy()
        for ingredient, amount in recipes[robot_type].items():
            clone_inv[ingredient] -= amount
        clone_robots[robot_type] += 1
        results.append(maximize(datas, clone_inv, clone_robots, time - 1))
        if robot_type == "geode" or robot_type == "obsidian":
            break

    results.append(maximize(datas, new_inv, new_robots, time - 1, set(can_be_produced)))

    return max(results)


best = 1
for data in datas:
    inv = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    robot = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    result = maximize(data, inv, robot, 32)
    print(data[0], result)
    best *= result
print(best)
