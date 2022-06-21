file = open("2020\day8\input.txt", "r")
lines = file.readlines()

globalVar = 0
linesVisited = []
linesChanged = {}

def CheckVisited(i, nopOrJmp):
    if(i in linesVisited and nopOrJmp):
        if i in linesChanged and not linesChanged[i]:
            linesVisited.append(i)
            return False
        if i in linesChanged:
            if "nop" in lines[i]:   
                lines[i] = lines[i].replace("nop", "jmp")
            else:
                lines[i] = lines[i].replace("jmp", "nop")  
            # print(linesChanged[i])  
            linesChanged[i] = False
            # print(linesChanged[i])  
            linesVisited.clear()
            # print(lines[i])
            return True
        # print(lines[i])
        linesVisited.clear()
        linesChanged[i] = True
        if "nop" in lines[i]:
            lines[i] = lines[i].replace("nop", "jmp")
        else:
            lines[i] = lines[i].replace("jmp", "nop")
        # print(lines[i])
        return True
                    
    else:
        linesVisited.append(i)
        return False

i = 0
while True:
    try:
        if "nop" in lines[i]:
            if CheckVisited(i, True):
                i = 0
                globalVar = 0
                continue
            i += 1
            continue
        if "acc" in lines[i]:
            var = int(lines[i][5:].strip("\n"))
            if "-" in lines[i]:
                globalVar -= var
            else:
                globalVar += var   
            i += 1
            continue
        if "jmp" in lines[i]:
            if CheckVisited(i, True):
                i = 0
                globalVar = 0
                continue
            var = int(lines[i][5:])
            if "-" in lines[i]:
                i -= var
            else:
                i += var
            continue
    except IndexError:
        print(globalVar)
        break
        
