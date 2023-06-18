import math
with open("2022\day3\input.txt", "r") as file:
    lines = [line.strip() for line in file]

new_set = {}
total = 0
for line in lines:
    new_set = {a for a in line[:math.floor(len(line) / 2)]}
    for item in line[math.floor(len(line) / 2):]:
        if item in new_set:
            if item.islower():
                total += ord(item) - 96
            else:
                total += ord(item) - 38
            break

print(total)
