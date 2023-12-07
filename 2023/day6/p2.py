with open("2023\day6\input.txt", "r") as file:
    lines = [line.strip() for line in file]

time = int("".join([x for x in lines[0].split(" ")[1:] if x != ""]))
distance = int("".join([x for x in lines[1].split(" ")[1:] if x != ""]))

left = 0
right = 0
for time_held in range(1, time):
    distance_cleared = time_held * (time - time_held)
    if distance_cleared > distance:
        left = time_held
        break
for time_held in range(time, 1, -1):
    distance_cleared = time_held * (time - time_held)
    if distance_cleared > distance:
        right = time_held
        break

print(right - left + 1)
