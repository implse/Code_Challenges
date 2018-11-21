f = open("sample/input1.txt", "r+")
lines = list()
for line in f:
    lines.append(line.rstrip())
f.close()

n_students = int(lines[0])
slots = lines[1:]
slots_students = list()
for s in slots:
    a, b = s.split(" ")
    slots_students.append((int(a), int(b)))
    slots_students.sort()

# Get all permutations of slots
perm_slots = []
def permute(lst, choosen = []):
    global perm_slots
    # Base Case
    if len(lst) == 0:
        #print(choosen)
        perm_slots.append(choosen.copy())
        choosen = []
    else:
        for i in range(len(lst)):
          # Choose
          c = lst.pop(i)
          # Explore
          for j in c:
            choosen.append(j)
            permute(lst, choosen)
            # Un-choose
            choosen.pop()
          lst.insert(i, c)

# Check if slots valid return count of possible students
def is_valid(perm):
    endAt = perm[0] + 60
    count_students = 0
    for i in range(1, len(perm)):
        if endAt < perm[i]:
            count_students += 1
    return count_students

# Final function
def students(perm_slots):
    max_students = 0
    for p in perm_slots:
        max_students = max(max_students, is_valid(p))
    return max_students

# Function call
permute(slots_students, choosen = [])
print(perm_slots)
max_students = students(perm_slots)
print(max_students)
