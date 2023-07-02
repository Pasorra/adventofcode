with open(r"2022\day10\input.txt", "r") as file:
    lines = [[x for x in line.strip().split()] for line in file]

register = 1
cycle = 0
k = 0


def check(cycle, k, register, result):
    if cycle != 0 and (cycle % (20 + (k*40)) == 0):
        return (result + (cycle * register), k + 1)
    return (result, k)


result = 0
for instruction in lines:
    if instruction[0] == "addx":
        cycle += 1
        result, k = check(cycle, k, register, result)
        cycle += 1
        result, k = check(cycle, k, register, result)

        register += int(instruction[1])

    elif instruction[0] == "noop":
        cycle += 1
        result, k = check(cycle, k, register, result)

print(result)
