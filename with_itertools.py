import sys
import itertools
import create_tuples as ct

num_points = int(sys.argv[1])
num_dimensions = int(sys.argv[2])

points = ct.create_random_tuples(num_points, num_dimensions)
pairs = []
for i in itertools.combinations(points, 2):
    pairs.append(i)
