file = open("2020\day11\input.txt", "r")
lines = file.readlines()

layout = [[char for char in x.strip("\n")] for x in lines]
lines.clear()
# layout = [x.strip("\n") for x in lines]
newLayout = []

def CheckAdjacent(posX, posY):
    seatsOccupied = 0
    for x in range(posX + -1, posX + 2):
        for y in range(posY + -1, posY + 2):
            try:
                if (x == posX and y == posY) or x < 0 or y < 0:
                    continue
                if layout[x][y] == "#":
                    seatsOccupied += 1
            except:
                continue
    
    return seatsOccupied

while True:
    changedSeats = 0
    for x, line in enumerate(layout):
        newLayout.append([])
        for y, dot in enumerate(line):
            if dot == ".":
                newLayout[x].append(dot)
                continue
            seatsOccupied = CheckAdjacent(x, y)
            if dot == "L" and seatsOccupied == 0:
                changedSeats += 1
                newLayout[x].append("#")
            elif seatsOccupied >= 4:
                changedSeats += 1
                newLayout[x].append("L")
            else: newLayout[x].append(dot)
    if newLayout == layout:
        print(newLayout)
        break
    layout = newLayout.copy()
    # print("".join(["".join(x) + "\n" for x in layout]), end="    ---    \n")
    newLayout.clear()

print(sum(["".join(x).count("#") for x in layout]))
                
                