number = "1"

# Read Input (line by line)
lines = list()
f = open("sample/input"+ number + ".txt", "r+")
n = f.read()
f.close()
lines = n.split("\n")
# print(lines)

# Read Output
output = list()
f = open("sample/output" + number + ".txt", "r+")
n = f.read()
f.close()
output = n.split("\n")
print(output)

n, m = lines[0].split(" ")

# Adjacency list: relations between friends
adjacency_list = dict()
for item in lines[1:]:
    value_1, value_2 = item.split(" ")
    if value_1 not in adjacency_list:
        adjacency_list[value_1] = set()
    if value_2 not in adjacency_list:
        adjacency_list[value_2] = set()
    adjacency_list[value_1].add(value_2)
    adjacency_list[value_2].add(value_1)

# Condition : adjacency_list["1"] exist or not
if "1" not  in adjacency_list:
    print(-1)
else:
    # Find intersection between friends set() and "1" set()
    my_friends = adjacency_list["1"]
    count_friends = []
    for id in my_friends:
        friends_intersection = len(adjacency_list["1"].intersection(adjacency_list[id]))
        count_friends.append((id, friends_intersection))
    max_so_far = 0
    id_max = -1
    # Looking for max common friends and max Id
    for id, friends in count_friends:
        id = int(id)
        friend = int(friends)
        if friends > max_so_far:
            max_so_far = friends
            id_max = id
        elif friends == max_so_far:
            if max_so_far == 0:
                continue
            id_max = max(id, id_max)
    print(id_max)
