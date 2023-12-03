with open("2022\day1\input.txt", "r") as file:
    lines = [line.strip() for line in file]

highest = 0
temp = 0
for line in lines:
    if line == "":
        highest = temp if temp > highest else highest
        temp = 0
        continue
    temp += int(line)

print(highest)
