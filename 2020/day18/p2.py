file = open("2020\day18\input.txt", "r")
lines = file.readlines()


operations = ["*", "+", "/", "-"]


def evaluate(exp: str):
    nums = []
    ops = []
    exp = exp.split()
    i = 0
    for e in exp:
        if e not in operations:
            nums.append(e)
        else:
            ops.append([e, i])
            i += 1
    # for o in ops:
    #     nums[1] = eval(f"{str(nums[0])} {o} {str(nums[1])}")
    #     nums.pop(0)
    for o in ops[::-1]:
        if o[0] != "+":
            continue
        nums[o[1]] = eval(f"{str(nums[o[1]])} {o[0]} {str(nums[o[1] + 1])}")
        ops.pop(o[1])
        nums.pop(o[1] + 1)
    for o in ops:
        nums[1] = eval(f"{str(nums[0])} {o[0]} {str(nums[1])}")
        nums.pop(0)
    return nums[0]


sumOfResults = 0
for inp in lines:
    while any(op in inp for op in operations):
        par1 = inp.rfind("(")
        if par1 != -1:
            par2 = par1 + inp[par1:].find(")")
            result = evaluate(inp[par1 + 1:par2])
            inp = inp[:par1] + str(result) + inp[par2 + 1:]
        else:
            sumOfResults += evaluate(inp)
            break

print(sumOfResults)
