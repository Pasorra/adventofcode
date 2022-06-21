file = open("2020\day5\input.txt", "r")
lines = file.readlines()

highestID = -1

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
    
    seatID = (rowL * 8) + colL
    highestID = seatID if seatID > highestID else highestID

print(highestID)
    
    
            
             
