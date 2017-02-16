import random

def create_random_tuples(num_tuples, dimensions):
    result = []
    for _ in range(num_tuples):
        tup = []
        for _ in range(dimensions):
            tup.append(random.randint(-100, 100))
        result.append(tuple(tup))
    return result
