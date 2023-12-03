with open("2023\day3\input.txt", "r") as file:
    lines = [line.strip() for line in file]


def check_for_numbers(line, i, checkedIs):
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
        if symbol != "*":
            continue

        nums = []
        checkedIs = []
        if row > 0:
            nums.append(check_for_numbers(lines[row - 1], i - 1, checkedIs))
            nums.append(check_for_numbers(lines[row - 1], i, checkedIs))
            nums.append(check_for_numbers(lines[row - 1], i + 1, checkedIs))

        checkedIs = []
        nums.append(check_for_numbers(lines[row], i - 1, checkedIs))
        nums.append(check_for_numbers(lines[row], i + 1, checkedIs))

        checkedIs = []
        if row + 1 < len(lines):
            nums.append(check_for_numbers(lines[row + 1], i - 1, checkedIs))
            nums.append(check_for_numbers(lines[row + 1], i, checkedIs))
            nums.append(check_for_numbers(lines[row + 1], i + 1, checkedIs))

        res = 1
        count = 0
        for num in nums:
            if num == 0:
                continue
            count += 1
            res *= num
        if count == 2:
            result += res


print(result)
