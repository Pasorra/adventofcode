with open("2023\day4\input.txt", "r") as file:
    lines = [line.strip() for line in file]

result = 0
dic = {str(x): 1 for x in range(1, len(lines) + 1)}
for i, card in enumerate(lines, 1):
    columnIndex = card.find(":")
    card = card[columnIndex + 1 :].split(" | ")
    winning_numbers = card[0].split(" ")
    our_numbers = card[1].split(" ")

    res = 0
    for num in our_numbers:
        if num != "" and num in winning_numbers:
            res += 1
    for x in range(i + 1, i + 1 + res):
        dic[str(x)] += dic[str(i)]


print(sum(dic.values()))
