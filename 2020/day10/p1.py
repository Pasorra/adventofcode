file = open("2020\day10\input.txt", "r")
lines = file.readlines()

adapters = [int(x.strip("\n")) for x in lines]
adapters.sort()
builtInJoltage = adapters[-1] + 3

rating = 0
oneJolts = 0
threeJolts = 0

while True:
    if builtInJoltage == rating:
        break
    if rating + 1 in adapters:
        oneJolts += 1
        rating += 1
    else:
        rating += 3
        threeJolts += 1
    
print(threeJolts * oneJolts)
    