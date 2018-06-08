# https://codefights.com/interview-practice/task/rMe9ypPJkXgk3MHhZ/description

# Make the hash table's keys the possible sums (or a set containing the possible sums).
# Start empty, and add new coins to it. When adding a new coin, you only need to consider
# the results you get from adding coins to a previous possible result.


# def possibleSums(coins, quantity):
#     s = set()
#     mx = max(quantity)
#     idx = quantity.index(mx)
#     cc = [coins[idx]*x for x in range(mx+1)]
#     b = set(cc)
#     print(cc)
#     print(b)

def possibleSums(coins, quantity):
    cq = list()


# Test 1

coins = [10, 50, 100]
quantity = [1, 2, 1]

# 10 = 10
# 10 + 50 = 60
# 10 + 50 + 50 = 110
# 10 + 50 + 50 + 100 = 210
# 10 + 50 + 100 = 160
#
# 50 + 50 = 100
# 50 + 50 + 100 = 200
# 50 + 100 = 150
#
# 100 = 100
# 100 + 10 = 110

print(possibleSums(coins, quantity));
