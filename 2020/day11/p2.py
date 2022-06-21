file = open("2020\day11\input.txt", "r")
lines = file.readlines()

layout = [[char for char in x.strip("\n")] for x in lines]
lines.clear()
# layout = [x.strip("\n") for x in lines]
newLayout = []

def CheckLine(posX, posY, xPlus, yPLus):
    try:
        while True:
            posX += xPlus
            posY += yPLus
            if posX < 0 or posY < 0:
                return 0
            if layout[posX][posY] == "#":
                return 1
            elif layout[posX][posY] == "L":
                return 0
    except:
        return 0
        
        
        

def CheckAdjacent(posX, posY):
    seatsOccupied = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            seatsOccupied += CheckLine(posX, posY, x, y)
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
            elif seatsOccupied >= 5:
                changedSeats += 1
                newLayout[x].append("L")
            else: newLayout[x].append(dot)
    if newLayout == layout:
        # print(newLayout)
        break
    layout = newLayout.copy()
    # print("".join(["".join(x) + "\n" for x in layout]), end="    ---    \n")
    newLayout.clear()

print(sum(["".join(x).count("#") for x in layout]))
                
                