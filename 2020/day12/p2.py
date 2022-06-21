file = open("2020\day12\input.txt", "r")
lines = file.readlines()

moves = {"E": 0, "S": 0, "W": 0, "N": 0}
waypoint = "E:10,S:0,W:0,N:1"
rotations = ["E", "S", "W", "N"]

currentDir = 0

def MoveWaypoint(letter):
    waypoints = waypoint.split(",")
    for index, point in enumerate(waypoints):
        if letter not in point:
            continue
        waypoints[index] = letter + ":" + str(int(point[2:]) + int(inst[1]))
    return ",".join(waypoints).strip(",")

for inst in lines:
    if "F" in inst:
        waypoints = waypoint.split(",")
        for point in waypoints:
            moves[point[0]] += int(inst[1:]) * int(point[2:])
    elif "R" in inst:
        currentDir = int((currentDir + (int(inst[1:]) / 90)) % 4)
        waypoints = waypoint.split(",")
        for index, point in enumerate(waypoints):
            waypoints[index] = rotations[currentDir] + point[1:] + ","
            currentDir += 1
            if(currentDir == 4):
                currentDir = 0
        waypoint = "".join(waypoints).strip(",")  
    elif "L" in inst:
        currentDir = int((currentDir - (int(inst[1:]) / 90)) % 4)
        # currentDir = int(abs(currentDir - ) % 4)
        waypoints = waypoint.split(",")
        for index, point in enumerate(waypoints):
            waypoints[index] = rotations[currentDir] + point[1:] + ","
            currentDir += 1
            if(currentDir == 4):
                currentDir = 0
        waypoint = "".join(waypoints).strip(",")
    elif "W" in inst:
        # waypoint["W"] += int(inst[1:])
        waypoint = MoveWaypoint("W")
    elif "E" in inst:
        waypoint = MoveWaypoint("E")
    elif "S" in inst:
        waypoint = MoveWaypoint("S")
    elif "N" in inst:
        waypoint = MoveWaypoint("N")

print(abs(moves["E"] - moves["W"]) + abs(moves["N"] - moves["S"]))