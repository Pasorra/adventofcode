with open("2022\day1\input.txt", "r") as file:
    lines = [line.strip() for line in file]

arr = []

temp = 0
for line in lines:
    if line == "":
        arr.append(temp)
        temp = 0
        continue
    temp += int(line)

arr.sort(reverse=True)
print(sum(arr[:3]))
