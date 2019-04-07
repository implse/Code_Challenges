# Given a sorted list rotated k times, return the index where the “unrotated” list would begin.

# Rotation Linear Search
def rotation_point_1(rotated_list):
  min_value = rotated_list[0]
  for i in range(1, len(rotated_list)):
    min_value = min(min_value, rotated_list[i])
  return rotated_list.index(min_value)

# Rotation  Binary Search
def rotation_point_2(rotated_list):
  low = 0
  high = len(rotated_list) - 1
  while low <= high:
    mid = (low + high) // 2
    mid_next = (mid + 1) % len(rotated_list)
    mid_previous = (mid - 1) % len(rotated_list)
    if rotated_list[mid] < rotated_list[mid_next] and rotated_list[mid] < rotated_list[mid_previous]:
      return mid
    if rotated_list[mid] < rotated_list[high]:
      high = mid - 1
    else:
      low = mid + 1
  return None

a = ['c', 'd', 'e', 'f', 'a'] # should return 4

print(rotation_point_2(a))
