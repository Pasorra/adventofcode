with open(r"2022\day8\input.txt", "r") as file:
    lines = [[int(x) for x in line.strip()] for line in file]

forest = [[0 for _ in line] for line in lines]

# left
for y in range(len(lines)):
    biggest = -1
    for x in range(len(lines[0])):
        val = lines[y][x]
        if biggest >= val:
            forest[y][x] = 1
        else:
            forest[y][x] = 0
            biggest = val


# top
for x in range(len(lines[0])):
    biggest = -1
    for y in range(len(lines)):
        val = lines[y][x]
        if biggest >= val:
            continue
        else:
            forest[y][x] = 0
            biggest = val


# right
for y in range(len(lines)):
    biggest = -1
    for x in range(len(lines[0])):
        val = lines[y][len(lines[0]) - x - 1]
        if biggest >= val:
            continue
        else:
            forest[y][len(lines[0]) - x - 1] = 0
            biggest = val

# bottom
for x in range(len(lines[0])):
    biggest = -1
    for y in range(len(lines)):
        val = lines[len(lines) - y - 1][x]
        if biggest >= val:
            continue
        else:
            forest[len(lines) - y - 1][x] = 0
            biggest = val

totalInvisible = len(lines) * len(lines[0])

for arr in forest:
    totalInvisible -= sum(arr)

print(totalInvisible)
