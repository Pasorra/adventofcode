file = open("2020\day6\input.txt", "r")
lines = file.readlines()
groups = []
group = []

def CheckLetterInAllGroups(group, letter):
    for word in group:
        if letter not in word:
            return False
    return True

for i, line in enumerate(lines):
    if line == "\n":
        group = sorted(group, key=len)
        groups.append(group.copy())
        group.clear()
        continue
    if i == len(lines) - 1:
        group.append(list(set(line)))
        group = sorted(group, key=len)
        groups.append(group.copy())
        break
    group.append(list(set(line[:-1])))
   
count = 0
for group in groups:
    if(len(group) == 1):
        count += len(group[0])
        continue
    groupAns = group[0]
    for letter in groupAns:
        if CheckLetterInAllGroups(group[1:], letter):
            count+= 1
            
print(count)

