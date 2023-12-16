with open("2023\day9\input.txt", "r") as file:
    lines = [line.strip() for line in file]

dataset = [[int(y) for y in x.split(" ")] for x in lines]


def all_zeroes(nums):
    for num in nums:
        if num != 0:
            return False
    return True


def check(data):
    if all_zeroes(data):
        return 0
    new_data = []
    for i in range(len(data) - 1):
        new_data.append(data[i + 1] - data[i])
    return data[0] - check(new_data)


results = []
for data in dataset:
    results.append(check(data))

print(sum(results))
