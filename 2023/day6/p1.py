with open("2023\day6\input.txt", "r") as file:
    lines = [line.strip() for line in file]

times = [int(x) for x in lines[0].split(" ")[1:] if x != ""]
distances = [int(x) for x in lines[1].split(" ")[1:] if x != ""]

final_res = 1
for i in range(len(times)):
    res = 0
    for time_held in range(1, times[i]):
        distance_cleared = time_held * (times[i] - time_held)
        if distance_cleared > distances[i]:
            res += 1
    final_res *= res
print(final_res)
