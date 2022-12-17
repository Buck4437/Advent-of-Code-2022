with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])


def find_min_dst(start, end, graph):
    queue = {start}
    visited = set()
    dst = 0
    while len(queue) > 0:
        if end in queue:
            return dst
        new_queue = set()
        for node in queue:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    new_queue.add(neighbour)
        queue = new_queue
        dst += 1
    return -1


def reduce_graph(graph, relevant_valves):
    reduced_graph = {}
    for start in relevant_valves:
        reduced_graph[start] = {}
        for end in relevant_valves:
            if start != end:
                dst = find_min_dst(start, end, graph)
                reduced_graph[start][end] = dst
    return reduced_graph


memoization_paths = {}


def find_all_possible_paths(graph, start="AA", dst=26, visited=None):
    if visited is None:
        visited = []
    if dst <= 0:
        return [tuple()]

    memoization_key = (start, dst, tuple(sorted(visited)))
    if memoization_key in memoization_paths:
        return memoization_paths[memoization_key]

    # Not moving is also a possible path
    all_paths = [tuple()]
    for neigh in graph[start]:
        if neigh in visited:
            continue
        remaining_dst = dst - (graph[start][neigh] + 1)
        if remaining_dst < 0:
            continue
        paths = find_all_possible_paths(graph, neigh, remaining_dst, visited + [neigh])
        for path in paths:
            all_paths.append((neigh, ) + path)
    memoization_paths[memoization_key] = all_paths
    return all_paths


def calc_pressure(graph, flow_rates, path, dst=26):
    total = 0
    path = ("AA", ) + path
    for i in range(1, len(path)):
        start, end = path[i-1], path[i]
        dst -= (graph[start][end] + 1)
        total += dst * flow_rates[end]
    return total


def get_pressure_lst(graph, flow_rates, path, dst=26):
    total = 0
    path = ("AA", ) + path
    for i in range(1, len(path)):
        start, end = path[i-1], path[i]
        dst -= (graph[start][end] + 1)
        total += dst * flow_rates[end]
    return total


def main():
    graph = {}
    flow_rates = {}

    for data in s.split("\n"):
        valve = data[6:8]
        flow_rate = int(data[data.find("=") + 1:data.find(";")])
        if "to valves " in data:
            tunnels = data.split("to valves ")[1].split(", ")
        else:
            tunnels = data.split("to valve ")[1].split(", ")
        flow_rates[valve] = flow_rate
        graph[valve] = []
        for tunnel in tunnels:
            graph[valve].append(tunnel)

    relevant_valves = []
    for valve, rate in flow_rates.items():
        if valve == "AA" or rate != 0:
            relevant_valves.append(valve)

    # Contains edge length
    reduced_graph = reduce_graph(graph, relevant_valves)

    part1(reduced_graph, flow_rates)
    part2(reduced_graph, flow_rates, relevant_valves)


def part1(reduced_graph, flow_rates):
    distance = 30
    paths = find_all_possible_paths(reduced_graph, dst=distance)
    max_pressure = 0
    best_path = tuple()
    for path in paths:
        pressure = calc_pressure(reduced_graph, flow_rates, path, dst=distance)
        if pressure > max_pressure:
            max_pressure = pressure
            best_path = path
            print(path, pressure)
    print("Part 1 final result:", max_pressure, best_path)


def part2(reduced_graph, flow_rates, relevant_valves):
    distance2 = 26

    paths = find_all_possible_paths(reduced_graph, dst=distance2)
    paths2 = []
    pressures = {}

    for path in paths:
        key = tuple(sorted(path))
        pressure = calc_pressure(reduced_graph, flow_rates, path, dst=distance2)
        if key not in pressures:
            pressures[key] = pressure
            paths2.append(key)
        elif pressure > pressures[key]:
            pressures[key] = pressure
    paths = paths2

    containment = dict([(valve, {}) for valve in relevant_valves])
    for path in paths:
        for valve in relevant_valves:
            containment[valve][path] = (valve in path)

    max_pressure = 0
    best_path = [tuple(), tuple()]
    for i in range(len(paths)):
        if i % 100 == 0:
            print(i)
        for j in range(i+1, len(paths)):
            path, path2 = paths[i], paths[j]
            if len(set(path) & set(path2)) == 0:
                pressure = pressures[path] + pressures[path2]
                if pressure > max_pressure:
                    max_pressure = pressure
                    best_path = [path, path2]
                    print([path, path2], pressure)
    print("Part 2 final result:", max_pressure, best_path)


main()
