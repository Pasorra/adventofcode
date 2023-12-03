with open("2023\day1\input.txt", "r") as file:
    lines = [line.strip() for line in file]

result = 0
for line in lines:
    num = 0
    found_first = False
    lastNum = -1

    for i, character in enumerate(line):
        if character.isdigit():
            if not found_first:
                num += 10 * int(character)
                found_first = True
            lastNum = int(character)

    num += lastNum
    result += num

print(result)
