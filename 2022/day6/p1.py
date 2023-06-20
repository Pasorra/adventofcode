with open("2022\day6\input.txt", "r") as file:
    lines = [line for line in file]
line = lines[0]
for i in range(len(line)):
    arr = line[i:i+4]
    _set = set(arr)
    if len(_set) == 4:
        print(i + 4)
        break
