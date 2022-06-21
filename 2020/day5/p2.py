file = open("2020\day5\input.txt", "r")
lines = file.readlines()

OCCUPIED_IDS = []

for line in lines:
    rowL = 0
    rowR = 127
    rowSeats = 64
    colL = 0
    colR = 7
    colSeats = 4
    for i in range(7):
        if line[i] == "F":
            rowR = rowR - rowSeats
            rowSeats /= 2
        elif line[i] == "B":
            rowL = rowR - rowSeats + 1
            rowSeats /= 2
    
    for i in range(7, 10):
        if line[i] == "L":
            colR = colR - colSeats
            colSeats /= 2
        elif line[i] == "R":
            colL = colR - colSeats + 1
            colSeats /= 2    
    
    OCCUPIED_IDS.append((rowL * 8) + colL)

OCCUPIED_IDS.sort()

for i in range(len(OCCUPIED_IDS)):
    if OCCUPIED_IDS[i + 1] - OCCUPIED_IDS[i] == 2:
        print(OCCUPIED_IDS[i] + 1)
        break