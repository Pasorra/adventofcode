file = open("2020\day12\input.txt", "r")
lines = file.readlines()

moves = {"E": 0, "S": 0, "W": 0, "N": 0}
rotations = ["E", "S", "W", "N"]

currentDir = 0

for inst in lines:
    if "F" in inst:
        moves[rotations[currentDir]] += int(inst[1:])
    elif "R" in inst:
        currentDir = int((currentDir + (int(inst[1:]) / 90)) % 4)
    elif "L" in inst:
        currentDir = int((currentDir - (int(inst[1:]) / 90)) % 4)
    elif "W" in inst:
        moves["W"] += int(inst[1:])
    elif "E" in inst:
        moves["E"] += int(inst[1:])
    elif "S" in inst:
        moves["S"] += int(inst[1:])
    elif "N" in inst:
        moves["N"] += int(inst[1:])

print(abs(moves["E"] - moves["W"]) + abs(moves["N"] - moves["S"]))