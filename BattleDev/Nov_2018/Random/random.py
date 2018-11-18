f = open("sample/input6.txt", "r+")
lines = list()
for line in f:
    lines.append(line.rstrip())
f.close()


n, points = lines
n = int(n) / 2
points = points.split(" ")
points = list(map(lambda x: int(x), points))


def random_fn(lst, n):
    cross_points = 0
    for i in range(len(lst) - 1):
        if (lst[i] == lst[i + 1] and n == lst[i]):
            return "INF"
        elif (lst[i] < n and lst[i + 1] >= n) or (lst[i] > n and lst[i + 1] <= n) :
            cross_points += 1
    return cross_points

print(random_fn(points, n))
