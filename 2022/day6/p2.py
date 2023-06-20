with open("2022\day6\input.txt", "r") as file:
    lines = [line for line in file]
line = lines[0]
for i in range(len(line)):
    arr = line[i:i+14]
    _set = set(arr)
    if len(_set) == 14:
        print(i + 14)
        break
