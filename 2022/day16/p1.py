with open(r"2022\day16\input.txt", "r") as file:
    lines = [line.strip() for line in file]

class Valve:
    def __init__(self, name: str, flow: int, valves: list) -> None:
        self.name = name
        self.flow = flow
        self.valves = valves
        self.open = False
        self.visited = False

def find_shortest_path(valve, to, valves, x = 0):
    returned = float("inf")
    for i, sub_valve in enumerate(valve.valves):
        if type(sub_valve) is str:
            sub_valve = find_valve(sub_valve, valves)
            valve.valves[i] = sub_valve
        
        if sub_valve == to:
            returned = min(x + 1, returned)
        elif not sub_valve.visited:
            sub_valve.visited = True
            returned = min(find_shortest_path(sub_valve, to, valves, x + 1), returned)
            sub_valve.visited = False
    return returned 
     
current:Valve
valves = []
for line in lines:
    line = line.split()
    name = line[1]
    flow = int(line[4].split("=")[1][:-1])
    sub_valves = "".join(line[9:]).split(",")
    valve = Valve(name, flow, sub_valves)
    valves.append(valve)
    if name == "AA":
        current = valve
    
def find_valve(target_name, valves):
    for valve in valves:
        if valve.name == target_name: return valve
    raise Exception

minute = 30
releasing = 0
valves.sort(key= lambda v: v.flow, reverse= True)
while True:
    possible_releases = []
    for valve in valves:
        if valve.flow == 0: break
        if valve.open == True: continue
        shortest = find_shortest_path(current, valve, valves) + 1 
        print(shortest)
        x = (30 - shortest) * valve.flow
        possible_releases.append([x, valve, shortest])
    if not possible_releases:
        break
    possible_releases.sort(key = lambda v: v[0], reverse=True)
    for arr in possible_releases:
        if arr[2] > minute: continue
        result += arr[0]
        minute -= arr[2]
        current = arr[1]
        current.open = True
        break
        
print(result)
