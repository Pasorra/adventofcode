with open("2023\day4\input.txt", "r") as file:
    lines = [line.strip() for line in file]

result = 0
for card in lines:
    columnIndex = card.find(":")
    card = card[columnIndex + 1 :].split(" | ")
    winning_numbers = card[0].split(" ")
    our_numbers = card[1].split(" ")
    res = 1 / 2
    for num in our_numbers:
        if num != "" and num in winning_numbers:
            res *= 2
    if res != 1 / 2:
        print(res)
        result += res

print(result)
