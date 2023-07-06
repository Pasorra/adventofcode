
######################################################################################################################
class Node:
    def __init__(self, x, y, elevation) -> None:
        self.x = x
        self.y = y
        self.parent: Node = None # type: ignore
        self.g_cost = 0
        self.h_cost = 0
        
    def get_f_cost(self):
        return self.g_cost + self.h_cost

    def get_distance(self, node):
        # return ((self.y - node.y)**2 + (self.x - node.x)**2)**(1/2)
        # return abs(self.y - node.y) + abs(self.x - node.x)
        raise NotImplementedError

    def get_neighbors(self, nodes):
        neighbors = []
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            
            if 0 <= new_x < len(nodes[0]) and 0 <= new_y < len(nodes):
                neighbor = nodes[new_y][new_x]
                neighbors.append(neighbor)
        raise NotImplementedError
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
######################################################################################################################
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
