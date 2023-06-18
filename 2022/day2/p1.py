with open("2022\day2\input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0

for line in lines:
    me = ord(line[2]) - 88
    opponent = ord(line[0]) - 65
    total += me + 1
    if (me - 1) % 3 == opponent:
        total += 6
    elif me == opponent:
        total += 3


print(total)
