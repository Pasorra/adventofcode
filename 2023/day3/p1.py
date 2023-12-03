with open("2023\day3\input.txt", "r") as file:
    lines = [line.strip() for line in file]


def check(line, i, checkedIs):
    if i in checkedIs:
        return 0
    arr = []
    x = i
    while x >= 0 and line[x].isdigit():
        if x in checkedIs:
            return 0
        arr.insert(0, int(line[x]))
        checkedIs.append(x)
        x -= 1
    x = i
    first = True
    while x < len(line) and line[x].isdigit():
        if first:
            first = False
            x += 1
            continue
        if x in checkedIs:
            return 0
        arr.append(int(line[x]))
        x += 1
    if len(arr) == 0:
        return 0
    res = 0
    for power, num in enumerate(arr[::-1]):
        res += num * pow(10, power)
    return res


result = 0
for row in range(len(lines)):
    for i in range(len(lines[row])):
        symbol = lines[row][i]
        if symbol.isdigit() or symbol == ".":
            continue

        checkedIs = []
        if row > 0:
            result += check(lines[row - 1], i - 1, checkedIs)
            result += check(lines[row - 1], i, checkedIs)
            result += check(lines[row - 1], i + 1, checkedIs)

        checkedIs = []
        result += check(lines[row], i - 1, checkedIs)
        result += check(lines[row], i + 1, checkedIs)

        checkedIs = []
        if row + 1 < len(lines):
            result += check(lines[row + 1], i - 1, checkedIs)
            result += check(lines[row + 1], i, checkedIs)
            result += check(lines[row + 1], i + 1, checkedIs)

print(result)
