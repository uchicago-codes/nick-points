import sys
import create_tuples as ct

num_points = int(sys.argv[1])
num_dimensions = int(sys.argv[2])

points = ct.create_random_tuples(num_points, num_dimensions)
pairs = []
for i in range(num_points - 1):
    for j in range(i, num_points):
        pairs.append((points[i], points[j]))
