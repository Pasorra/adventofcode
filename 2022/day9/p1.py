with open(r"2022\day9\input.txt", "r") as file:
    lines = [[x for x in line.strip().split()] for line in file]


def check_distance(head, tail, head_last):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        tail = head_last.copy()
        visited.add((tail[0], tail[1]))  # type: ignore

    return tail


head = [0, 0]
head_last = [0, 0]
tail = [0, 0]
visited = set((0, 0))

for operation in lines:
    for i in range(int(operation[1])):
        head_last = head.copy()
        if operation[0] == "R":
            head[0] += 1
        elif operation[0] == "L":
            head[0] -= 1
        elif operation[0] == "U":
            head[1] += 1
        elif operation[0] == "D":
            head[1] -= 1
        tail = check_distance(head, tail, head_last)

print(len(visited))
