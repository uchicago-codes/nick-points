import sys
import itertools
import point

def parse_file(filepath):
    points = []
    with open(filepath, 'r') as point_file:
        for line in point_file.readlines():
            data = line.rstrip().split(',')
            name = data[0]
            coordinates = tuple(float(coord) for coord in data[1:])
            points.append(point.Point(name, coordinates))
    return points

def find_closest_to_origin(points):
    origin_coords = tuple(0 for i in range(points[0].dimensions))
    origin = point.Point('origin', origin_coords)
    closest = None
    min_distance = float('inf')
    for current_point in points:
        dist = current_point.distance_from(origin)
        if dist < min_distance:
            closest = current_point
            min_distance = dist
    return (closest, min_distance)

def find_closest_pair(points):
    closest = None
    min_distance = float('inf')
    for pair in itertools.combinations(points, 2):
        dist = pair[0].distance_from(pair[1])
        if dist < min_distance:
            closest = pair
            min_distance = dist
    return (closest, min_distance)

def main(input_file):
    points = parse_file(input_file)
    closest = find_closest_to_origin(points)
    print 'Closest point to origin: %s (%.2f)' % (closest[0].name, closest[1])
    closest_pair = find_closest_pair(points)
    point1 = closest_pair[0][0]
    point2 = closest_pair[0][1]
    dist = closest_pair[1]
    print 'Closest pair: %s, %s (%.2f)' % (point1.name, point2.name, dist)


if __name__ == '__main__':
    points_file = sys.argv[1]
    main(points_file)
