#!/usr/bin/env python

from math import sqrt
import operator


class Point(object):
    """A 2-D point"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return '<Point %d, %d>' % (self._x, self._y)

    @classmethod
    def distance(cls, point1, point2):
        """Return distance between two Point instances"""
        return sqrt((point1._x - point1._x) ^ 2 +
                    (point1._y - point2._y) ^ 2)


ALL_POINTS = []

def addPoint(point):
    """
    Add a 2D point to some internal data structure.
    """
    ALL_POINTS.append(point)



def findClosest(center, num_points):
    """
    Out of the added points, find the "numPoints" closest points to "center".
    """
    points_list = []

    for point in ALL_POINTS:
        distance = Point.distance(center, point)
        points_list.append({'point': point, 'distance': distance})

    ret = []

    sorted_points_list = sorted(points_list, key=operator.itemgetter('distance'))
    for i in range(num_points):
        ret.append(sorted_points_list[i]['point'])

    return ret


p1 = Point(3, 5)
p2 = Point(5, 6)
p3 = Point(8, 1)
p4 = Point(7, 3)
addPoint(p1)
addPoint(p2)
addPoint(p3)
addPoint(p4)
print(ALL_POINTS)
print(Point.distance(p1, p2))

print(findClosest(p1, 2))
