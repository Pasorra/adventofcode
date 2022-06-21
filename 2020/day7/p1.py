import re

file = open("2020\day7\input.txt", "r")
lines = file.readlines()
totalBags = []

def SearchBag(bag):
    bags = []
    count = 0
    if(bag[-1] == "s"):
        bag = bag[:-1]
    for line in lines:
        matchObj = re.search(" \d+ " + bag, line)
        if matchObj != None:
            # print(line[:matchObj.start()])
            newStr = line[:matchObj.start()].split(" contain")
            if(newStr[0] not in totalBags):
                totalBags.append(newStr[0])
                bags.append(newStr[0])
    for bag in bags:
        count += SearchBag(bag)
    return count + len(bags)

print(SearchBag("shiny gold bag"))

