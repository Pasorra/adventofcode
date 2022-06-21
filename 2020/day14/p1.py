file = open("2020\day14\input.txt", "r")
lines = file.readlines()

mask = {}
values = {}

def ReadMask(index):
    mask.clear()
    for i, byte in enumerate(lines[index][::-1].strip(" = ksam")):
        if byte == "X" or byte == "\n":
            continue
        mask[i - 1] = int(byte)

for index, line in enumerate(lines):
    if "mask" in line:
        ReadMask(index)
        continue
    partition = line.split(" = ")
    memChannel = int(partition[0].strip("mem[]"))
    val = [x for x in format(int(partition[1]), "036b")]
    val = val[::-1]
    for maskVal in mask:
        val[maskVal] = mask[maskVal]
    val = val[::-1]
    joinedVal = "".join(str(x) for x in val)
    values[memChannel] = int(joinedVal, 2) 

count = 0

for val in values:
    count += values[val]

print(count)