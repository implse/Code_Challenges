# Solution with Counter
from collections import Counter

n = int(lines[0])
colors = lines[1:]

rank = Counter(colors)
first_color, second_color = rank.most_common(2)

print(first_color, second_color)


# Solution with a Max Heap
from collections import Counter
import heapq

n = int(lines[0])
colors = lines[1:]

color1, color2 = heapq.nlargest(2, [(color, score) for color, score in Counter(colors.items()])

print(color1[1], color2[1])


# Solution classic
n = int(lines[0])
colors = lines[1:]

# dictionary of color: score
rank = dict()
for i in range(n):
    color = colors[i]
    if color not in rank:
        rank[color] = 1
    else:
        rank[color] += 1

first_color = ""
first_score = 0
second_color = ""
second_score = 0

# First color
for color, score in rank.items():
    if score > first_score:
        first_score = score
        first_color = color

rank[first_color] *= -1

# Second color
for color, score in rank.items():
    if score > second_score:
        second_score = score
        second_color = color

rank[second_color] *= -1

print(first_color, second_color)
