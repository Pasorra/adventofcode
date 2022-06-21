file = open("2020\day9\input.txt", "r")
lines = file.readlines()

sumOfTwoNums = []

def Sum(index):
    i = 25
    sumOfTwoNums.clear()
    for x in range(index, index + 25):
        num = int(lines[x].strip("\n"))
        for y in range(x + 1, x + i):
            secondNum = int(lines[y].strip("\n"))
            sumOfTwoNums.append(num + secondNum)
        i -= 1

def FindInvalidNumber():    
    for i in range(25, len(lines)):
        Sum(i - 25)
        if int(lines[i].strip("\n")) not in sumOfTwoNums:
            print(lines[i].strip("\n"))
            return int(lines[i].strip("\n"))
    
def FindWeakness():
    weakArr = []
    for x in range(len(lines)):
        dummyArray = []
        dummyArray.append(int(lines[x].strip("\n")))
        for y in range(x + 1, len(lines)):
            dummyArray.append(int(lines[y].strip("\n")))
            summedArray = sum(dummyArray)
            if summedArray > invalidNumber:
                break
            if summedArray == invalidNumber:
                if len(weakArr) < len(dummyArray):
                    weakArr = dummyArray.copy()
    weakArr.sort()
    return weakArr[0] + weakArr[-1]

invalidNumber = FindInvalidNumber()
print(FindWeakness())
        
        