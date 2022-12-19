from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

datas = ints(s, False, True)


def maximize(datas, inv, robots, time):

    idx, ore, clay, obs1, obs2, geode1, geode2 = datas

    new_inv = inv.copy()
    new_robots = robots.copy()

    if time <= 0:
        return new_inv["geode"]

    if time == 1:
        return new_inv["geode"] + new_robots["geode"]

    if time >= 20:
        print(time)

    # Too many robots = bad, too many items = also bad

    if new_robots["ore"] > max([clay, obs1, geode1]):
        return 0

    if new_inv["ore"] > max([clay, obs1, geode1]) * 3:
        return 0
    
    if new_robots["clay"] > obs2:
        return 0

    if new_inv["clay"] > obs2 * 3:
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
        clone_inv, clone_robots = new_inv.copy(), new_robots.copy()
        for ingredient, amount in inputs.items():
            if clone_inv[ingredient] < amount:
                break
        else:
            can_be_produced.append(robot_type)

    for key, value in robots.items():
        new_inv[key] += value

    for robot_type in can_be_produced:
        clone_inv, clone_robots = new_inv.copy(), new_robots.copy()
        for ingredient, amount in recipes[robot_type].items():
            clone_inv[ingredient] -= amount
        clone_robots[robot_type] += 1
        results.append(maximize(datas, clone_inv, clone_robots, time - 1))
        if robot_type == "geode" or robot_type == "obsidian":
            break

    # Not buying robots will lead to too much materials being stocked, which is inefficient.
    results.append(maximize(datas, new_inv, new_robots, time - 1))

    return max(results)


qualities = 0
for data in datas:
    inv = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    robot = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    best = maximize(data, inv, robot, 24)
    quality = best * data[0]
    print(data[0], best)
    qualities += quality
print(qualities)

