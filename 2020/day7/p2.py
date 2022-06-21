import re

file = open("2020\day7\input.txt", "r")
lines = file.readlines()
totalBags = {}

def SearchBag(bag):
    finalCount = 0
    if("bags" not in bag):
        bag += "s"
    if "other" in bag:
        return 0 
    for line in lines:
        matchObj = re.search(bag + " contain", line)
        if matchObj != None:
            newStr = line[matchObj.end():].split(",")
            for eachBag in newStr:
                eachBag = eachBag.strip(" ,\n.")
                count = sum([int(s) for s in eachBag.split() if s.isdigit()])
                if eachBag[2:] not in totalBags:
                    returnedCount = SearchBag(eachBag[2:])
                    totalBags[eachBag[2:]] = returnedCount
                    finalCount += count + (count * returnedCount)
                else:
                    finalCount += count + (count * totalBags[eachBag[2:]])
            break         
    return finalCount 

print(SearchBag("shiny gold bag"))
