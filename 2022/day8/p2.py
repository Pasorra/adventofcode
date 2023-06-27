import numpy as np

with open(r"2022\day8\input.txt", "r") as file:
    lines = [[int(x) for x in line.strip()] for line in file]

lines = np.array(lines)
forest = np.zeros(lines.shape)


def calculate_scenic(slice, val):
    count = 0
    for i in slice:
        count += 1
        if i >= val:
            return int(count)
    return int(count)


for index, val in np.ndenumerate(lines):
    if 0 in index or lines.shape[0] - 1 == index[0] or lines.shape[1] - 1 == index[1]:
        continue
    x, y = index
    left = np.flip(lines[x, 0:y])
    right = lines[x, y + 1:]
    up = np.flip(lines[0:x, y])
    down = lines[x + 1:, y]
    forest[x, y] = calculate_scenic(left, val) * calculate_scenic(
        right, val) * calculate_scenic(up, val) * calculate_scenic(down, val)

print(int(np.max(forest)))
