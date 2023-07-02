import turtle

with open(r"2022\day10\input.txt", "r") as file:
    lines = [[x for x in line.strip().split()] for line in file]

register = 1
cycle = 1


def check_visible(cycle, register, positions: list):
    row = 5 - (cycle // 40)
    cycle %= 40
    if register == cycle:
        if [register, row] not in positions:
            positions.append([register, row])
    if register - 1 == cycle:
        if [register - 1, row] not in positions:
            positions.append([register - 1, row])
    if register + 1 == cycle:
        if [register + 1, row] not in positions:
            positions.append([register + 1, row])


positions = []
result = 0
for instruction in lines:
    if instruction[0] == "addx":
        check_visible(cycle - 1, register, positions)
        cycle += 1
        check_visible(cycle - 1, register, positions)
        cycle += 1

        register += int(instruction[1])

    elif instruction[0] == "noop":
        check_visible(cycle - 1, register, positions)
        cycle += 1


wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
turt = turtle.Turtle()

turt.up()
scale = 15
for pos in positions:
    turt.setpos((pos[0] - 20) * scale, pos[1] * scale)
    turt.write("@")

turtle.done()
