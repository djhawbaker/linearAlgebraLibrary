from math import sqrt, acos, pi

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
    """Add vector a and b together"""
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
    """Subtract vector b from vector a"""
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
    """Scale the vector by the input scalar"""
    z = []
    for x in vec:
        z.append(scalar * x)

    return z


def magnitude(vec):
    """Calculate the magnitude of the vector"""
    sqrd_coordinates = [x**2 for x in vec]
    return sqrt(sum(sqrd_coordinates))


def normalize(vec):
    """Normalize the vector"""
    try:
        m = magnitude(vec)
        return scaleVector(1/m, vec)

    except ZeroDivisionError:
        raise exception("Cannot normalize the zero vector")


def dot(a, b):
    """Calculate the dot product"""
    if len(a) == len(b):
        z = []
        for i in range(len(a)):
            z.append(a[i] * b[i])
        
        return sum(z)

    else:
        raise ValueError("Length of vectors must match")


def dotAngle(a, b):
    """Calculate the angle of the dot product"""
    if len(a) == len(b):
        d = dot(a, b)

        mag_a = magnitude(a)
        mag_b = magnitude(b)

        return acos(d/(mag_a * mag_b))
    
    else:
        raise ValueError("Length of vectors must match")


def isParallel(a, b):
    """Returns whether the two vectors are parallel or not
    Note: If vector is the 0 vector then it's parallel and orthogonal to itself and all other vectors
    """
    return ( is_zero(a) or
        is_zero(b) or
        dotAngle(a, b) == 0 or
        dotAngle(a, b) == pi )


    na = normalize(a)
    nb = normalize(b)
    if na == nb:
        return True
    else:
        return False


def isOrthogonal(a, b, tolerance=1e-10):
    """Returns whether the two vectors are orthogonal or not
    Note: If vector is the 0 vector then it's parallel and orthogonal to itself and all other vectors
    """
    return abs(dot(a,b)) < tolerance
    #if dot(a, b) == 0:
    #    return True
    #else:
    #    return False
    

def is_zero(vec, tolerance=1e-10):
    """Returns if the vector is the zero vector or not"""
    return magnitude(vec) < tolerance



def calcVecProjection(a, b):
    """Calculate the vector projection"""
    return dot(a, normalize(b))
    
