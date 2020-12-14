

import linear_algebra_lib as al

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    v = al.addVectors([8.218, -9.341], [-1.129, 2.111])
    print("Add: ", v)

    w = al.subtractVectors([7.119, 8.215], [-8.223, 0.878])
    print("Subtract: ", w)

    z = al.scaleVector(7.41, [1.671, -1.012, -0.318])
    print("Scale: ", z)

    print("Magnitude: ", al.magnitude([-0.221, 7.437]))
    print("Magnitude: ", al.magnitude([8.813, -1.331, -6.247]))

    print("Direction: ", al.normalize([5.581, -2.136]))
    print("Direction: ", al.normalize([1.996, 3.108, -4.554]))

    print("Dot ", al.dot([7.887, 4.138], [-8.802, 6.776]))

    print("Dot 2: ", al.dot([-5.955, -4.904, -1.874], [-4.496, -8.755, 7.103]))
    print("angle 1: ", al.dotAngle([3.183, -7.627], [-2.668, 5.319]))
    print("angle 2: ", al.dotAngle([7.35, 0.221, 5.188], [2.751, 8.259, 3.985]))


