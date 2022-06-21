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
    
for i in range(25, len(lines)):
    Sum(i - 25)
    if int(lines[i].strip("\n")) not in sumOfTwoNums:
        print(lines[i].strip("\n"))
        break
        
        