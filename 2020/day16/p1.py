file = open("2020\day16\input.txt", "r")
lines = file.readlines()

validNos = set()
invalidNos = []

index = 0

for i, line in enumerate(lines):
    if line == "\n":
        index = i        
        break
    splitline = "".join(line.split(":")[1])
    splitline = splitline.split(" or ")
    for split in splitline:
        split = split.split("-")
        for i in range(int(split[0]),int(split[1]) + 1):
            validNos.add(i)


for line in lines[i + 5:]:
    line = line.split(",")
    for num in line:
        if(int(num) not in validNos):
            invalidNos.append(int(num))
            
print(sum(invalidNos))