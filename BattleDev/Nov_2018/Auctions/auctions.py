f = open("sample/input1.txt", "r+")
lines = list()
for line in f:
    lines.append(line.rstrip())
f.close()

# number of bids
bids = int(lines[0])
# reserve price
reserve_price = int(lines[1])
# bidder's first name and bid price
bidders = lines[2:]

def winner(bidders, reserve_price):
    max_bid = 0
    max_name = ""
    for b in bidders:
        bid, name = (b.split(" "))
        if int(bid) > reserve_price and int(bid) > max_bid :
            max_name = name
            max_bid = int(bid)
    return max_name if max_bid > 0 else "KO"

print(winner(bidders, reserve_price))
