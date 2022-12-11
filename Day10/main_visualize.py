import time
import sys
import termcolor

with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])

puz_in = s.split("\n")
cycle = 1
x_val = 1
total = 0


def wait(t):
    t0 = time.time()
    while True:
        if time.time() - t0 > t:
            return


def clock():
    global cycle, total
    trace()
    if (cycle - 20) % 40 == 0:
        total += cycle * x_val
    cycle += 1
    wait(0.05)
    # waiting_time = max(0.03, (250 - cycle) / (500 * (cycle // 20 + 1)))
    # wait(waiting_time)


def execute(line):
    global x_val
    if "noop" == line:
        clock()
    else:
        val = int(line[5:])
        clock()
        clock()
        x_val += val


prev_output = ""
grid = ""
cursor = termcolor.colored("█", "yellow")
cyan_cursor = termcolor.colored("█", "cyan")


def get_header():
    return f"Op: {line:<9} Cycles: {cycle}, X register: {x_val}"


def get_sprite():
    return "".join(
        [cyan_cursor if abs(i - x_val) <= 1 else " " for i in range(40)]
    )


def get_raw_output(show_grid=True):
    if show_grid:
        raw_output = f"{get_header()}\n\n{get_sprite()}\n\n{grid}{cursor}"
    else:
        raw_output = f"{get_header()}\n\n{get_sprite()}\n\n{cursor}"
    raw_output += "\n" * (12 - raw_output.count("\n"))
    return raw_output


def trace():
    global grid
    column = ((cycle - 1) % 40)
    if abs(column - x_val) <= 1:
        grid += "█"
    else:
        grid += " "
    if cycle % 40 == 0:
        grid += "\n"

    output_stuff(get_raw_output())


def output_stuff(output):
    global prev_output
    sys.stdout.write("\r")
    for i in range(prev_output.count("\n")):
        sys.stdout.write("\033[A")
    sys.stdout.write(output)
    prev_output = output


line = ""
print("\n" * 30)
output_stuff(get_raw_output(show_grid=False))
wait(1)
for line in puz_in:
    execute(line)
# print(total)
