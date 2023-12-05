# not only is this extremely slow but also just straight up doesn't work... amazing.......................
import time

start = time.time()
with open(r"2022\day16\input.txt", "r") as file:
    lines = [line.strip() for line in file]


class Valve:
    def __init__(self, name: str, flow: int) -> None:
        self.name = name
        self.flow = flow
        self.valves = []
        self.open = False
        self.cost_to_move = 0


def find_valve_by_name(valves: list[Valve], name: str):
    return next(x for x in valves if x.name == name)


def bfs(source: Valve, destination: Valve, valves: list[Valve]):
    q = [source]
    for valve in valves:
        valve.cost_to_move = 0
    visited = []
    while q:
        valve = q.pop(0)
        visited.append(valve)
        if valve == destination:
            return valve.cost_to_move
        for new_valve in valve.valves:
            if new_valve not in visited:
                q.append(new_valve)
                new_valve.cost_to_move = valve.cost_to_move + 1
    return 0


valves: list[Valve] = []
startingValve: Valve
for line in lines:
    semicolonIndex = line.find(";")
    valve = Valve(line[6:8], int(line[23:semicolonIndex]))
    valves.append(valve)
    if valve.name == "AA":
        startingValve = valve

for line in lines:
    currentValve: Valve = find_valve_by_name(valves, line[6:8])
    valveNames = line.split(", ")
    valveNames[0] = valveNames[0][-2:]
    for valveName in valveNames:
        valve: Valve = find_valve_by_name(valves, valveName)
        currentValve.valves.append(valve)


def brute(start, i, value):
    values = [value]
    for valve in valves:
        if valve.flow == 0 or valve.open:
            continue
        cost = bfs(start, valve, valves) + 1
        if cost >= i:
            continue
        valve.open = True
        values.append(brute(valve, i - cost, value + ((i - cost) * valve.flow)))
        valve.open = False
    return max(values)


print(brute(startingValve, 30, 0))
print(time.time() - start)
