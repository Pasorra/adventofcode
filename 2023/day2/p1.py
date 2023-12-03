with open("2023\day2\input.txt", "r") as file:
    lines = [line.strip() for line in file]


def check(subset: str):
    numsAndColors = subset.split(", ")
    redCubes = 12
    greenCubes = 13
    blueCubes = 14
    for cubes in numsAndColors:
        cubes = cubes.split(" ")
        if cubes[1] == "red":
            redCubes -= int(cubes[0])
            if redCubes < 0:
                return False
        elif cubes[1] == "green":
            greenCubes -= int(cubes[0])
            if greenCubes < 0:
                return False
        elif cubes[1] == "blue":
            blueCubes -= int(cubes[0])
            if blueCubes < 0:
                return False
    return True


result = 0
for gameID, game in enumerate(lines, 1):
    startOfPartition = game.index(":") + 2
    subsets = game[startOfPartition:].split("; ")
    for subset in subsets:
        if not check(subset):
            break
    else:
        result += gameID

print(result)
