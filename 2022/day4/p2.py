with open("2022\day4\input.txt", "r") as file:
    lines = [line.strip() for line in file]

count = 0

for line in lines:
    line = line.split(",")
    line_left = sorted([int(x) for x in line[0].split("-")])
    line_right = sorted([int(x) for x in line[1].split("-")])
    left_first = line_left[0]
    left_second = line_left[1]
    right_first = line_right[0]
    right_second = line_right[1]
    if left_first <= right_first <= left_second or left_first <= right_second <= left_second:
        count += 1
        continue
    elif right_first <= left_first <= right_second or right_first <= left_second <= right_second:
        count += 1
        continue

print(count)
