with open("2023\day8\input.txt", "r") as file:
    lines = [line.strip() for line in file]


class Node:
    def __init__(self, name: str):
        self.name = name
        self.left: Node = None
        self.right: Node = None


def find_node_by_name(nodes: list[Node], name: str):
    return next(x for x in nodes if x.name == name)


instructions = lines[0]
nodes: list[Node] = []
current_node = None

for node in lines[2:]:
    root = node[:3]
    nodes.append(Node(root))

for node in lines[2:]:
    root = node[:3]
    left = node[7:10]
    right = node[12:15]
    root_node = find_node_by_name(nodes, root)
    left_node = find_node_by_name(nodes, left)
    right_node = find_node_by_name(nodes, right)
    root_node.left = left_node
    root_node.right = right_node
    if root == "AAA":
        current_node = root_node

turns = 0
i = 0
while True:
    if current_node.name == "ZZZ":
        break

    if instructions[i] == "R":
        current_node = current_node.right
    else:
        current_node = current_node.left
    i = (i + 1) % len(instructions)
    turns += 1

print(turns)
