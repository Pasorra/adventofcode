with open("2022\day2\input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0
for line in lines:
    me = ord(line[2]) - 88
    opponent = ord(line[0]) - 65
    match me:
        case 0:
            total += ((opponent - 1) % 3) + 1
        case 1:
            total += opponent + 4
        case 2:
            total += ((opponent + 1) % 3) + 7

print(total)
