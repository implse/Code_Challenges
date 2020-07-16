# Serie de Cartes

n = int(lines[0])
cards = lines[1:]

max_so_far = -1

for i in range(n):
    current_count = 1
    for j in range(i+1, n):
        if cards[i] == cards[j]:
            current_count += 1
        else:
            break
    max_so_far = max(current_count, max_so_far)

print(max_so_far)
