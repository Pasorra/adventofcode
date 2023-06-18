file = open("2020\day17\input.txt", "r")
lines = file.readlines()

coordinates = {}
newCoordinates = {}


def checkNeighbors(coor, isActive):
    trueNeighbors = 0
    for z in range(coor[2] - 1, coor[2] + 2):
        for y in range(coor[1] - 1, coor[1] + 2):
            for x in range(coor[0] - 1, coor[0] + 2):
                if [x, y, z] == coor:
                    continue
                if f"{x},{y},{z}" in coordinates:
                    trueNeighbors += 1
                if trueNeighbors > 3:
                    return
    if isActive and (trueNeighbors == 2 or trueNeighbors == 3):
        newCoordinates[f"{coor[0]},{coor[1]},{coor[2]}"] = True
    elif trueNeighbors == 3:
        newCoordinates[f"{coor[0]},{coor[1]},{coor[2]}"] = True


for y in range(len(lines)):
    for x in range(len(lines[0]) - 1):
        if lines[y][x] == "#":
            coordinates[f"{x},{y},{0}"] = True

for _ in range(6):
    print(len(coordinates))
    for coor in coordinates.items():
        coor = coor[0].split(",")
        coor = [int(x) for x in coor]
        trueNeighbors = 0
        for z in range(coor[2] - 1, coor[2] + 2):
            for y in range(coor[1] - 1, coor[1] + 2):
                for x in range(coor[0] - 1, coor[0] + 2):
                    if [x, y, z] == coor:
                        continue
                    if f"{x},{y},{z}" in coordinates:
                        trueNeighbors += 1
                        checkNeighbors([x, y, z], True)
                    else:
                        checkNeighbors([x, y, z], False)
        if trueNeighbors == 2 or trueNeighbors == 3:
            newCoordinates[f"{coor[0]},{coor[1]},{coor[2]}"] = True
    coordinates = newCoordinates.copy()
    newCoordinates.clear()


print(len(coordinates))
