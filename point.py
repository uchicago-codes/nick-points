"""docstring"""

class Point(object):
    """
    Represents an n-dimensional point

    Attributes:
        name (str): Human-readable string describing the point
        coordinates (tuple): n-dimensional tuple representing a point
        dimensions (int): count of dimensions of coordinates tuple
    """

    def __init__(self, name, coordinates):
        """
        Args:
            name (str): Human-readable string describing the point
            coordinates (tuple): n-dimensional tuple representing a point
        """
        self.name = name
        self.coords = coordinates
        self.dimensions = len(coordinates)

    def distance_from(self, point):
        """
        Calculates the Euclidean distance between two n-dimensional points:
            1. The instance of Point
            2. Another instance of Point

        Args:
            point (Point): an instance of the Point class

        Exceptions:
            TypeError: Raised if dimensions between two points differ
        """

        if self.dimensions != point.dimensions:
            raise TypeError('Different dimensions')
        dims = range(self.dimensions)
        return sum((self.coords[i] - point.coords[i]) ** 2.0 for i in dims) ** 0.5
