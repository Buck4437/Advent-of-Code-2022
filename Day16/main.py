from aoc import *
from collections import defaultdict

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


def maximize_pressure(graph, flow_rates, start="AA", dst=30, visited=None):
    if visited is None:
        visited = set()
    if dst <= 0:
        return [], 0
    best_path, best_pressure = [], 0
    for neigh in graph[start]:
        if neigh not in visited:
            # One extra minute to open a valve
            path_len = graph[start][neigh] + 1
            if path_len > dst:
                continue
            remaining_time = dst - path_len

            new_visited = visited | {neigh}
            sub_path, sub_pressure = maximize_pressure(graph, flow_rates, neigh, remaining_time, new_visited)
            pressure = sub_pressure + remaining_time * flow_rates[neigh]
            if pressure > best_pressure:
                best_path, best_pressure = [neigh] + sub_path, pressure
    # Returns the best path, followed by total pressure
    return best_path, best_pressure


memoization = {}


def maximize_pressure_2(graph, flow_rates, starts=("AA", "AA"), dsts=(26, 26), visited=None):
    if visited is None:
        visited = set()

    memoization_key = (starts, dsts, tuple(sorted(visited)))
    if memoization_key in memoization:
        return memoization[memoization_key]

    s1, s2 = starts
    d1, d2 = dsts
    if d1 <= 0 and d2 <= 0:
        return [[], []], 0
    best_path, best_pressure = [[], []], 0
    for neigh1 in graph[s1]:
        if neigh1 in visited:
            continue
        for neigh2 in graph[s2]:
            if neigh2 in visited or neigh1 == neigh2:
                continue
            neighs = [neigh1, neigh2]
            new_starts, new_dsts = [], []
            new_visited = visited
            no_move = []
            for i in range(2):
                start, neigh, dst = starts[i], neighs[i], dsts[i]
                path_len = graph[start][neigh] + 1
                if path_len > dst:
                    # It should not move
                    new_starts.append(start)
                    new_dsts.append(dst)
                    no_move.append(True)
                else:
                    new_starts.append(neigh)
                    new_dsts.append(dst - path_len)
                    new_visited = new_visited | {neigh}
                    no_move.append(False)
            if all(no_move):
                continue
            sub_path, sub_pressure = maximize_pressure_2(graph, flow_rates, tuple(new_starts), tuple(new_dsts), new_visited)
            pressure = sub_pressure
            for i in range(2):
                if not no_move[i]:
                    pressure += new_dsts[i] * flow_rates[new_starts[i]]
            if pressure > best_pressure:
                best_path, best_pressure = [sub_path[i] if no_move[i] else ([new_starts[i]] + sub_path[i]) for i in range(2)], pressure
    memoization[memoization_key] = best_path, best_pressure
    # Returns the best path, followed by total pressure
    return best_path, best_pressure


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
    print(maximize_pressure(reduced_graph, flow_rates))
    print(maximize_pressure_2(reduced_graph, flow_rates))


main()
