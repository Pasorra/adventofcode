with open("2022\day5\input.txt", "r") as file:
    lines = [line for line in file]

crates = []
# create crates
start_index = 0
for index, val in enumerate(lines):
    if any(char.isdigit() for char in val):
        for i in range(index - 1, -1, -1):
            for letter in range(1, len(lines[i]), 4):
                if lines[i][letter] != " ":
                    try:
                        crates[letter//4].append(lines[i][letter])
                    except:
                        crates.append([lines[i][letter]])
        start_index = index + 2
        break


for i in range(start_index, len(lines)):
    line = lines[i].strip().split()
    for x in range(int(line[1])):
        val = crates[int(line[3]) - 1].pop()
        crates[int(line[5]) - 1].append(val)

print("".join([x[-1] for x in crates]))
