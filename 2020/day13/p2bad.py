file = open("2020\day13\input.txt", "r")
lines = file.readlines()

busDepartures = [int(x) if x != "x" else -1 for x in lines[1].split(",")]
busDuplicate = busDepartures.copy()
changedList = []
# busDepartures[0] = 0

while True:
    shouldContinue = False
    for i, num in enumerate(busDepartures):
        if i == 0:
            if any(changedList):
                changedList.clear()
                continue
            else:
                changedList.clear()
                busDepartures[i] += busDuplicate[i]
                continue
        if num == -1: continue
        if num <= busDepartures[0]:
            busDepartures[i] += busDuplicate[i]
            changedList.append(True)
            shouldContinue = True
            continue
        if num >= busDepartures[0]:
            changedList.append(False)
        if num - busDepartures[0] != i:
            shouldContinue = True
    if not shouldContinue:
        break

print(busDepartures[0])