with open("2022\day3\input.txt", "r") as file:
    lines = [line.strip() for line in file]


total = 0
for i in range(0, len(lines), 3):
    set1 = {a for a in "".join(lines[i])}
    set2 = {a for a in "".join(lines[i + 1])}
    set3 = {a for a in "".join(lines[i + 2])}
    for item in set1:
        if item in set2 and item in set3:
            if item.islower():
                total += ord(item) - 96
            else:
                total += ord(item) - 38
            break

print(total)
