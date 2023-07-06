import turtle

with open(r"2022\day14\input.txt", "r") as file:
    lines = [line.strip() for line in file]

world = set()
lowest = 0
for line in lines:
    coords = line.split(" -> ")
    for i in range(len(coords)- 1):
        coord1 = coords[i].split(",")
        coord2 = coords[i + 1].split(",")
        if coord1[0] == coord2[0]:
            world.update([(int(coord1[0]), x) for x in range(min(int(coord1[1]), int(coord2[1])), max(int(coord1[1]), int(coord2[1]))+1)])
        elif coord1[1] == coord2[1]:
            world.update([(x, int(coord1[1])) for x in range(min(int(coord1[0]), int(coord2[0])), max(int(coord1[0]), int(coord2[0]))+1)])
        lowest = max(max(int(coord1[1]), int(coord2[1])),lowest)


wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor("light green")
turt = turtle.Turtle(visible=False)
turt.up()

scale = 4.75
y_offset = 75
turt.speed(0)
for pos in world:
    turt.setpos((pos[0] - 500) * scale, (lowest - pos[1] - y_offset) * scale)
    turt.write("■")

sand_x = 500
sand_y = 0
sand_count = 0
i = False
turt.color("yellow")
while True:
    if (sand_x, sand_y) in world:
        print(sand_count)
        break
    i = True

    if ((sand_x, sand_y + 1) not in world) and (sand_y + 1 != lowest + 2):
        sand_y += 1
    elif ((sand_x -1, sand_y +1 ) not in world) and (sand_y + 1 != lowest + 2):
        sand_x -= 1
        sand_y += 1
    elif ((sand_x + 1, sand_y + 1) not in world) and (sand_y + 1 != lowest + 2):
        sand_x += 1
        sand_y += 1
    else:
        world.add((sand_x, sand_y))
        turt.setpos((sand_x - 500) * scale, (lowest - sand_y - y_offset) * scale)
        turt.write("●")
        sand_x = 500
        sand_y = 0
        sand_count += 1
        i = False
        
turtle.done()