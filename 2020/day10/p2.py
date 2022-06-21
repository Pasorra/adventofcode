file = open("2020\day10\input.txt", "r")
lines = file.readlines()

adapters = [int(x.strip("\n")) for x in lines]
adapters.sort()
builtInJoltage = adapters[-1] + 3

rating = 0
finalCount = 1
oneArrayToRuleThemAll = []

while True:
    count = -1
    arr = []
    if rating + 1 in adapters:
        count += 1
        arr.append(rating + 1)
    if rating + 2 in adapters:
        count += 1 
        arr.append(rating + 2)
    if rating + 3 in adapters:
        count += 1 
        arr.append(rating + 3)
    if len(arr) == 3:
        if arr[0] + 3 in adapters:
            finalCount *= 7
        elif arr[0] + 4 in adapters:
            finalCount *= 6
        elif arr[0] + 5 in adapters:
            finalCount *= 4
    elif len(arr) == 2:
        if arr[0] + 4 in adapters:
            finalCount *= 2
        elif arr[0] + 3 in adapters:
            finalCount *= 3
    if builtInJoltage == rating + 3:
        print(finalCount)
        break
    
    rating = arr[-1]
    
    

