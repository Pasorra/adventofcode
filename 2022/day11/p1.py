with open(r"2022\day11\input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

monkeys = {}
monkey = {"Starting Items": [], "Operation": "",
          "Test": "", "True": "", "False": "", "Inspected Times": 0}

id = 0
for line in lines:
    if line == []:
        monkeys[id] = monkey.copy()
        id += 1
        monkey = {"Starting Items": [], "Operation": "",
                  "Test": "", "True": "", "False": "", "Inspected Times": 0}
    elif "Starting" in line[0]:
        for item in line[::-1]:
            if "items" in item:
                break
            monkey["Starting Items"].append(int(item.removesuffix(",")))
    elif "Operation" in line[0]:
        monkey["Operation"] = "".join(line[-3:])
    elif "Test" in line[0]:
        monkey["Test"] = int(line[-1])
    elif "true" in line[1]:
        monkey["True"] = int(line[-1])
    elif "false" in line[1]:
        monkey["False"] = int(line[-1])

monkeys[id] = monkey.copy()

for _ in range(20):
    for monkey in monkeys.values():
        for _ in range(len(monkey["Starting Items"])):
            monkey["Inspected Times"] += 1
            old = monkey["Starting Items"].pop()
            item = eval(monkey["Operation"])
            item = item // 3
            if item % monkey["Test"] == 0:
                monkeys[monkey["True"]]["Starting Items"].append(item)
            else:
                monkeys[monkey["False"]]["Starting Items"].append(item)

largest = 0
second_largest = 0
for monkey in monkeys.values():
    times = monkey["Inspected Times"]
    if times > largest:
        if largest > second_largest:
            second_largest = largest
        largest = times
    elif times > second_largest:
        second_largest = times

print(largest * second_largest)
