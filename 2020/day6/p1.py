file = open("2020\day6\input.txt", "r")
lines = file.readlines()
groups = []
group = []

for line in lines:
    if(line == "\n"):
        groups.append(len(group))
        group.clear()
    for char in line:
        if(len(group) == 26):
            break
        if(char not in group and char != "\n"):
            group.append(char)
groups.append(len(group))
    
print(sum(groups)) 