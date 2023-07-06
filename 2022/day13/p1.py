import ast

with open(r"2022\day13\input.txt", "r") as file:
    lines = [line.strip() for line in file]

def compare_values(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return "correct"
        elif right < left:
            return "wrong"
        else :
            return "continue"
    elif type(left) is int and type(right) is list:
        return compare_values([left], right)
    elif type(right) is int and type(left) is list:
        return compare_values(left, [right])
    elif type(left) is list and type(right) is list:
        min_index = min(len(left), len(right))
        for i in range(min_index):
            result = compare_values(left[i], right[i])
            if result != "continue":
                return result
        if len(left) < len(right):
            return "correct"
        if len(right) < len(left):
            return "wrong"
        return "continue"

def check_list(left, right):
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        left_value = left[left_index]
        right_value = right[right_index]
        result = compare_values(left_value, right_value)
        if result == "continue":
            left_index += 1
            right_index += 1
        else:
            return result
    if len(left) == left_index and len(right) == right_index:
        return "continue"
    elif len(left) == left_index:
        return "correct"
    else:
        return "wrong"



pairs = []
current_pair = []
for line in lines:
    if line:
        current_pair.append(ast.literal_eval(line))
    else:
        pairs.append(current_pair)
        current_pair = []

count = 0
for i, pair in enumerate(pairs, 1):
    left, right = pair
    result = check_list(left, right)
    if result == "correct":
        count += i

print(count)
