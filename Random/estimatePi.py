# Estimate Pi value with Monte Carlo method. (random sampling)

import math

# Euclidian distance between two points
def euclidian_distance(x1, y1, x2, y2):
  return math.sqrt((x1-x2)**2 + (y1+y2)**2)

# Generate random points
def create_random_points(n):
  points = list()
  for i in range(n):
    x = random.random()
    y = random.random()
    points.append((x, y))
  return points

# Estimate Pi
def estimate_pi(n):
  points = create_random_points(n)
  inside_circle = 0
  for point in points:
    if euclidian_distance(point[0], point[1], 0, 0) <= 1:
      inside_circle += 1
  return 4 * inside_circle / n

print(estimate_pi(100000))
