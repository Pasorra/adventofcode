from time import sleep
import turtle

with open(r"2022\day9\input.txt", "r") as file:
    lines = [[x for x in line.strip().split()] for line in file]

window = turtle.Screen()
window.bgcolor("light green")
turt = turtle.Turtle(visible=False)
turt.up()


def check_distance(rope, i=1):
    if i == 10:
        return

    distX = rope[i - 1][0] - rope[i][0]
    distY = rope[i - 1][1] - rope[i][1]
    if abs(distX) + abs(distY) == 3 or abs(distX) + abs(distY) == 4:
        rope[i][0] += 1 if distX > 0 else -1
        rope[i][1] += 1 if distY > 0 else -1
        check_distance(rope, i + 1)
    elif abs(distX) == 2:
        rope[i][0] += 1 if distX > 0 else -1
        check_distance(rope, i + 1)
    elif abs(distY) == 2:
        rope[i][1] += 1 if distY > 0 else -1
        check_distance(rope, i + 1)
    if i == 9:
        visited.add((rope[i][0], rope[i][1]))  # type: ignore
        vis.append(rope[i].copy())


rope = [[0, 0] for _ in range(10)]
head_last = [0, 0]
visited = set((0, 0))
vis = []
x = 0
for operation in lines:
    for i in range(int(operation[1])):
        x += 1
        head_last = rope[0].copy()
        if operation[0] == "R":
            rope[0][0] += 1
        elif operation[0] == "L":
            rope[0][0] -= 1
        elif operation[0] == "U":
            rope[0][1] += 1
        elif operation[0] == "D":
            rope[0][1] -= 1
        check_distance(rope)
    # turt.clear()
    # turt.goto(0, 0)
    # turt.write("s", align="center")

    # for i, pos in enumerate(rope):
    #     turt.goto(pos[0]*20, pos[1]*20)
    #     turt.write(str(i), align="center")
    # sleep(.25)

# turt.clear()
# for pos in vis:
#     turt.goto(pos[0], pos[1])
#     turt.write("#", align="center")
# sleep(0.25)
# turtle.done()

arr = []
count = 0
for pos in vis:
    if pos not in arr:
        count += 1
        arr.append(pos)

print(count)
