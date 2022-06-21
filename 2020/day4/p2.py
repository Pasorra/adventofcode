import re

file = open("2020\day4\input.txt", "r")
lines = file.readlines()
lines.append("\n")
newLines = []
validCount = 0
FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

newStr = ""
for line in lines:
    if line == "\n":
        newLines.append(newStr)
        newStr = ""
        continue
    newStr += line.replace("\n", " ")
newLines[len(newLines) - 1] += " "

def CheckField(val, field):
    match field:
        case "byr":
            return (int(val) >= 1920 and int(val) <= 2002)
        case "iyr":
            return (int(val) >= 2010 and int(val) <= 2020)
        case "eyr":
            return (int(val) >= 2020 and int(val) <= 2030)
        case "hgt":
            if("cm" in val):
                return (int(val[:-2]) >= 150 and int(val[:-2]) <= 193)
            elif("in" in val):
                return (int(val[:-2]) >= 59 and int(val[:-2]) <= 76)
            return False
        case "hcl":
            if(len(val) != 7): return False
            return re.search("#([a-f]|[0-9]){6}", val)
        case "ecl":
            if(len(val) != 3): return False
            return re.search("amb|blu|brn|gry|grn|hzl|oth", val)
        case "pid":
            if(len(val) != 9): return False
            return re.search("\d{9}", val)
            

for line in newLines:
    failed = False
    for field in FIELDS:
        if (failed): break
        if(field not in line):
            failed = True
            break
        
        i = line.index(field)
        startIndex = line.index(":", i) + 1
        endIndex = line.index(" ", i)
        substring = line[startIndex:endIndex]
        failed = not CheckField(substring, field)
        
    if not failed: validCount += 1
print(validCount)