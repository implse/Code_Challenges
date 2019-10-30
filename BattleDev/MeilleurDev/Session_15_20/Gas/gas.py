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

gas_capacity = int(lines[0])
conso = int(lines[1])
gas_stations = list(map(lambda x : int(x), lines[2:]))
destination = int(lines[-1])
distance_full_gas = (gas_capacity / conso) * 100
distance_between_station = 0
finish = True
for station in gas_stations:
    distance_between_station = station - distance_between_station
    if distance_between_station > distance_full_gas:
        finish = False
        break
    distance_between_station = station
print("OK") if finish == True else print("KO")
