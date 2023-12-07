with open("2023\day5\input.txt", "r") as file:
    lines = [line.strip() for line in file]

# seed number and whether it was checked
seeds = [[int(x), False] for x in lines[0].split(" ")[1:]]
i = 3
while i < len(lines):
    if lines[i] == "":
        i += 2
        for seed in seeds:
            seed[1] = False
        continue
    line = [int(x) for x in lines[i].split(" ")]
    for seed in seeds:
        # if we found the seed in a map previously, continue
        if seed[1]:
            continue
        if line[1] <= seed[0] < line[1] + line[2]:
            seed[1] = True
            seed[0] = line[0] + (seed[0] - line[1])

    i += 1

print(min(seeds, key=lambda x: x[0])[0])
