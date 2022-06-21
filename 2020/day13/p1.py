file = open("2020\day13\input.txt", "r")
lines = file.readlines()

earliest = int(lines[0])
busDepartures = lines[1].split(",")
needToWait = earliest
busID = 0

for depart in busDepartures:
    if depart == "x":
        continue
    x = int(earliest / int(depart))
    x = (x + 1) * int(depart)
    if x - earliest  < needToWait:
        needToWait = x - earliest
        busID =  int(depart)

print(busID * needToWait)