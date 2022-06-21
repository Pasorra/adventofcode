#67,7,59,61
solve = [67,  7, 59, 61]
    #    335  #294   #1829  
    #   +469x +413y  +3599z 
dummySolve = []

def Solve(a, b, diff):
    m = x = y = 0
    arr = []
    while True:
        res = a * x - b * y
        # print(res)
        if res == diff: 
            # print(x, y, ":" ,a * x, b * y)
            arr.append(a * x)
            if len(arr) == 1: m = arr[0] 
            if len(arr) >= 2: break
        if res >= 0: y += 1
        else: x += 1

    print(arr[1] - arr[0], m)
    dummySolve.append(m)
    
i = 0
while True:
    if len(solve) == 1:
        break
    if i == len(solve)- 1:
        solve = dummySolve.copy()
        dummySolve.clear()
        i = 0
        continue
    Solve(solve[i], solve[i+1])
    i += 1