import ast

with open(r"2022\day13\input.txt", "r") as file:
    lines = [line.strip() for line in file]

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            result = compare_values(lst[j], lst[j + 1])
            if result == "wrong":
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

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



pairs = [[[2]], [[6]]]
for line in lines:
    if line:
        pairs.append(ast.literal_eval(line))
    
bubble_sort(pairs)
result = 1
for i, pair in enumerate(pairs, 1):
    if pair == [[2]] or pair == [[6]]:
        result *= i

print(result)