from math import sqrt, acos

#class LinearAlgebraLib():
#    """Library for my linear algebra functions"""

#    def __init__(self):
#        """Constructor - Creates the library"""

def plus(self, v):
    new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)


def minus(self, v):
    new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)

def times_scalar(self, c):
    new_coordinates = [c*x for x in self.coordinates]
    return Vector(new_coordinates)


def addVectors(a, b):


    l = 0
    if len(a) == len(b):
        l = len(a)
    else:
        raise ValueError

    z = []
    for x in range(l):
        z.append(a[x] + b[x])

    return z

def subtractVectors(a,b):
    l = 0
    if len(a) == len(b):
        l = len(a)
    else:
        raise ValueError

    z = []
    for x in range(l):
        z.append(a[x] - b[x])

    return z

def scaleVector(scalar, vec):
    z = []
    for x in vec:
        z.append(scalar * x)

    return z

def magnitude(vec):
    sqrd_coordinates = [x**2 for x in vec]
    return sqrt(sum(sqrd_coordinates))

def normalize(vec):
    try:
        m = magnitude(vec)
        return scaleVector(1/m, vec)

    except ZeroDivisionError:
        raise exception("Cannot normalize the zero vector")

def dot(a, b):

    if len(a) == len(b):
        z = []
        for i in range(len(a)):
            z.append(a[i] * b[i])
        
        return sum(z)

    else:
        raise ValueError("Length of vectors must match")


def dotAngle(a, b):

    if len(a) == len(b):
        d = dot(a, b)

        mag_a = magnitude(a)
        mag_b = magnitude(b)

        return acos(d/(mag_a * mag_b))
    
    else:
        raise ValueError("Length of vectors must match")
