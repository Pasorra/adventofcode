with open(r"2022\day12\input.txt", "r") as file:
    lines = [line.strip() for line in file]


class Node:
    def __init__(self, x, y, elevation) -> None:
        self.x = x
        self.y = y
        self.elevation = elevation
        self.parent: Node = None # type: ignore
        self.g_cost = 0
        self.h_cost = 0
        
    def get_f_cost(self):
        return self.g_cost + self.h_cost

    def get_distance(self, node):
        # return ((self.y - node.y)**2 + (self.x - node.x)**2)**(1/2)
        return abs(self.y - node.y) + abs(self.x - node.x)

    def get_neighbors(self, nodes):
        neighbors = []
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            
            if 0 <= new_x < len(nodes[0]) and 0 <= new_y < len(nodes):
                neighbor = nodes[new_y][new_x]
                elevation_diff = neighbor.elevation - self.elevation 
                
                if elevation_diff <= 1:
                    neighbors.append(neighbor)
        
        return neighbors

def a_star(start: Node, end: Node, nodes:list[list[Node]]):
    open_nodes: list[Node] = [start]
    closed_nodes: list[Node]= []
    
    while open_nodes:
        current: Node = min(open_nodes, key=lambda n: (n.get_f_cost(), n.g_cost))
        open_nodes.remove(current)
        closed_nodes.append(current)
                
        if current == end:
            print("Found it!")
            return
        
        neighbors: list[Node] = current.get_neighbors(nodes)
        
        for neighbor in neighbors:
            if neighbor in closed_nodes:
                continue
            
            movement_cost_to_neighbor = current.g_cost + current.get_distance(neighbor)

            if (movement_cost_to_neighbor < neighbor.g_cost) or (neighbor not in open_nodes):
                neighbor.g_cost = movement_cost_to_neighbor
                neighbor.h_cost = neighbor.get_distance(end)
                neighbor.parent = current
                
                if neighbor not in open_nodes:
                    open_nodes.append(neighbor)
    
    raise Exception("Could not find")

nodes: list[list[Node]] = [[Node(-1, -1, -10) for x in y] for y in lines]
start: Node = None # type: ignore
target: Node = None # type: ignore

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            node = Node(x, y, 0)
            nodes[y][x] = node
            start = node
            continue
        elif char == "E":
            node = Node(x, y, 25)
            target = node
            nodes[y][x] = node
            continue
        nodes[y][x] = Node(x, y, ord(char) - 97)

a_star(start, target, nodes)

a = target
count = 0
while a != start:
    count += 1
    a = a.parent

print(count)