from time import sleep


with open(r"2022\day15\input.txt", "r") as file:
    lines = [line.strip() for line in file]

def collapse(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])

    result = []
    for current in ranges:
        if not result or current[0] > result[-1][1] + 1:
            result.append(current) 
        else:
            result[-1][1] = max(result[-1][1], current[1])

    return result

possible_x = 0
possible_y = 0
for y in range(4000000):
    impossible = []
    beacons = set()
    for line in lines:
        line = line.split()
        sensor_x = int(line[2][2:-1])
        sensor_y = int(line[3][2:-1])
        beacon_x = int(line[8][2:-1])
        beacon_y = int(line[9][2:])
        beacons.add((beacon_x, beacon_y))
        
        distance_to_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        distance_to_y = abs(sensor_y - y)
        
        if distance_to_y > distance_to_beacon: continue

        n = distance_to_beacon - distance_to_y
        impossible.append([sensor_x - n, sensor_x + n])

    impossible = collapse(impossible)

    if len(impossible) > 1:
        print(impossible)
        possible_x = impossible[0][1] + 1
        possible_y = y
        break

print((possible_x * 4000000) + possible_y)