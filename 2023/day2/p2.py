with open("2023\day2\input.txt", "r") as file:
    lines = [line.strip() for line in file]


def check(subset: str):
    numsAndColors = subset.split(", ")
    redCubes = 0
    greenCubes = 0
    blueCubes = 0

    for cubes in numsAndColors:
        cubes = cubes.split(" ")
        if cubes[1] == "red":
            redCubes += int(cubes[0])
        elif cubes[1] == "green":
            greenCubes += int(cubes[0])
        elif cubes[1] == "blue":
            blueCubes += int(cubes[0])

    return {
        "red": redCubes,
        "green": greenCubes,
        "blue": blueCubes,
    }


result = 0
for gameID, game in enumerate(lines, 1):
    minCubes = {"red": 0, "green": 0, "blue": 0}
    startOfPartition = game.index(":") + 2
    subsets = game[startOfPartition:].split("; ")
    for subset in subsets:
        checkRes = check(subset)
        minCubes["red"] = max(minCubes["red"], checkRes["red"])
        minCubes["blue"] = max(minCubes["blue"], checkRes["blue"])
        minCubes["green"] = max(minCubes["green"], checkRes["green"])

    result += minCubes["red"] * minCubes["blue"] * minCubes["green"]

print(result)
