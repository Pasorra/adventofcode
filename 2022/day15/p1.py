with open(r"2022\day15\input.txt", "r") as file:
    lines = [line.strip() for line in file]

y = 2000000

def collapse(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])

    result = []
    for current in ranges:
        if not result or current[0] > result[-1][1] + 1:
            result.append(current) 
        else:
            result[-1][1] = max(result[-1][1], current[1])

    return result

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

beacons_on_line = 0
for beacon in beacons:
    if beacon[1] != y:
        continue
    for current in impossible:
        if current[0]<= beacon[0] <= current[1]:
            beacons_on_line += 1
            
total = 0
for impos in impossible:
    total += abs(impos[1] - impos[0]) + 1
print(total - beacons_on_line)