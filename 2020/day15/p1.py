file = open("2020\day15\input.txt", "r")
lines = file.readlines()

numbers = lines[0].split(",")
memory = dict()

for i, num in enumerate(numbers):
    memory[int(num)] = [i + 1] 

lastNum = int(numbers[-1])

def addToMemory():
    if lastNum in memory:
        memory[lastNum].append(i)
        if len(memory[lastNum]) > 2:
            memory[lastNum].remove(min(memory[lastNum]))
    else:
        memory[lastNum] = [i]

for i in range(len(numbers) + 1, 30000001):
    if lastNum not in memory or (lastNum in memory and len(memory[lastNum]) == 1):
        lastNum = 0
        addToMemory()
    else:
        lastNum = max(memory[lastNum]) - min(memory[lastNum])
        addToMemory()

print(lastNum)