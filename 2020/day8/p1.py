file = open("2020\day8\input.txt", "r")
lines = file.readlines()

globalVar = 0
linesVisited = []

def CheckVisited(i):
    if(i in linesVisited):
        print(globalVar)    
        return True
    else:
        linesVisited.append(i)
        return False

i = 0

while True:
    if "nop" in lines[i]:
        if CheckVisited(i):
            break
        i += 1
        continue
    if "acc" in lines[i]:
        if CheckVisited(i):
            break
        var = int(lines[i][5:].strip("\n"))
        if "-" in lines[i]:
            globalVar -= var
        else:
            globalVar += var   
        i += 1
        continue
    if "jmp" in lines[i]:
        if CheckVisited(i):
            break
        var = int(lines[i][5:])
        if "-" in lines[i]:
            i -= var
        else:
            i += var
        continue
        
