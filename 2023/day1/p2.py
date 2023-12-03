with open("2023\day1\input.txt", "r") as file:
    lines = [line.strip() for line in file]


def checkWordDigit(line, index):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, number in enumerate(numbers):
        if number == line[index : index + len(number)]:
            return i + 1
    return 0


result = 0
for line in lines:
    num = 0
    foundFirst = False
    lastNum = -1

    for i, character in enumerate(line):
        if character.isdigit():
            if not foundFirst:
                num += 10 * int(character)
                foundFirst = True
            lastNum = int(character)
        res = checkWordDigit(line, i)
        if res:
            if not foundFirst:
                num += 10 * res
                foundFirst = True
            lastNum = res

    num += lastNum
    result += num

print(result)
