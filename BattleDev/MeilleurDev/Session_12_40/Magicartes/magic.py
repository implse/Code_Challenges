# Test Select
number = "1"

# Read Input (line by line)
lines = list()
f = open("sample/input"+ number + ".txt", "r+")
n = f.read()
f.close()
lines = n.split("\n")
print(lines)

# Read Output
output = list()
f = open("sample/output" + number + ".txt", "r+")
n = f.read()
f.close()
output = n.split("\n")
print(output)

player_A = list(map(lambda x: int(x), lines[1].split(" ")))
player_B = list(map(lambda x: int(x), lines[2].split(" ")))

from collections import deque

player_A_deck = deque(player_A)
player_B_deck = deque(player_B)

while len(player_A_deck) > 0 or len(player_B_deck) > 0:
    card_A = player_A_deck.popleft() if len(player_A_deck) > 0 else 0
    card_B = player_B_deck.popleft() if len(player_B_deck) > 0 else 0 
    if card_A > card_B:
        player_A_deck.append(card_A)
    if card_A < card_B:
        player_B_deck.append(card_B)
    if card_A == card_B:
        if len(player_A_deck) == 0 and len(player_B_deck) == 0:
            print("N")
            break
        else:
            continue
    if len(player_A_deck) == 0:
        print("G")
        break
    if len(player_B_deck) == 0:
        print("P")
        break
