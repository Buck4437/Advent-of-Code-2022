from aoc import *

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

rocks = set()
tower_height = 0


# The floor is at row 0
# The walls are at column 0 and 8
def has_rock(r, c):
    if r >= 0 or c == 0 or c == 8:
        return True
    return (r, c) in rocks


def has_overlap(positions):
    for r, c in positions:
        if has_rock(r, c):
            return True
    return False


move_counter, rock_counter = 0, 0


rock_shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(-1, 0), (-2, 1), (-1, 1), (0, 1), (-1, 2)],
    [(0, 0), (0, 1), (-2, 2), (-1, 2), (0, 2)],
    [(-3, 0), (-2, 0), (-1, 0), (0, 0)],
    [(-1, 0), (0, 0), (-1, 1), (0, 1)]
]


def next_move():
    global move_counter
    val = s[move_counter]
    move_counter = (move_counter + 1) % len(s)
    return val


def next_rock():
    global rock_counter
    val = rock_shapes[rock_counter]
    rock_counter = (rock_counter + 1) % len(rock_shapes)
    return val


def find_unblocked_rocks():
    start = -tower_height-1, 1
    reachable = set()
    visited = set()
    queue = {start}
    while len(queue) > 0:
        new_queue = set()
        for pos in queue:
            for r, c in vecs_add([(1, 0), (0, -1), (0, 1)], pos):
                if c <= 0 or c >= 8 or r >= 0:
                    continue
                if (r, c) not in visited:
                    visited.add((r, c))
                    if has_rock(r, c) and 1 <= c <= 7:
                        reachable.add((r, c))
                    else:
                        new_queue.add((r, c))
        queue = new_queue
    return reachable


cycle_counter = 0
cycle_start = None
prev_states = []

while True:
    rock_pos = vecs_add(next_rock(), (-tower_height - 4, 3))
    while True:
        move = next_move()
        new_pos = vecs_add(rock_pos, (0, 1) if move == ">" else (0, -1))
        if not has_overlap(new_pos):
            rock_pos = new_pos
        down_pos = vecs_add(rock_pos, (1, 0))
        if has_overlap(down_pos):
            break
        else:
            rock_pos = down_pos
    for rock in rock_pos:
        rocks.add(rock)
    reachable_rocks = tuple(sorted(vecs_add(find_unblocked_rocks(), (tower_height, 0))))

    height_delta = max(tower_height, max([-pos[0] for pos in rock_pos])) - tower_height
    tower_height = tower_height + height_delta

    cur_state = ((rock_counter, move_counter, reachable_rocks), height_delta)

    if cur_state in prev_states:
        cycle_start = prev_states.index(cur_state)
        break
    prev_states.append(cur_state)
    cycle_counter += 1


cycle_length = len(prev_states) - cycle_start
start_delta = sum(state[1] for state in prev_states[:cycle_start])
cycle_delta = sum(state[1] for state in prev_states[cycle_start:])


def find_tower_height(moves):
    cycles = (moves - cycle_start) // cycle_length
    end_length = (moves - cycle_start) % cycle_length
    end_delta = sum(state[1] for state in prev_states[cycle_start:cycle_start + end_length])
    if moves < cycle_start:
        return start_delta
    return start_delta + cycle_delta * cycles + end_delta


print(find_tower_height(2022))
print(find_tower_height(1000000000000))
