from math import pi, sqrt, atan2, sin, cos

import numpy as np
import matplotlib.pyplot as plt

class Vector:
    """Creates a vector"""

    def __init__(self, *coordinates: float):
        self.coord = coordinates
        self.origin = tuple(0 for _ in range(len(coordinates)))

    def set_origin(self, *origin: float):
        self.origin = origin

    def get_angle(self) -> float:
        return sqrt(sum([v**2 for v in self.coord]))

    def __iter__(self):
        return iter(self.coord)
    
    def __mul__(self, scaler: float):
        coords = [c * scaler for c in self.coord]
        return Vector(*coords)

    def __getitem__(self, index: int) -> float:
        return self.coord[index]

    def __str__(self):
        coords = ', '.join(map(str, self.coord))
        return f"({coords})"

    def __add__(self, other):
        point = [a + b for a, b in zip(self.coord, other)]
        return Vector(*point)

    def __sub__(self, other):
        point = [a - b for a, b in zip(self.coord, other)]
        vector = Vector(*point)
        # vector.set_origin(other)
        return vector

class Matrix():
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
    
    def __mul__(self, other):
        if type(other) == Vector:
            vec_array = np.array(other.coord)
            transformed_vector = np.dot(self.matrix, vec_array)
            return Vector(*transformed_vector)
        elif type(other) == Matrix:
            pass


def draw2d(*vectors, lim=((-3, 6), (-3, 6))):
    plt.figure(figsize=(5, 5))
    plt.axhline(linewidth=0.5, color='#333')
    plt.axvline(linewidth=0.5, color='#333')
    cmap = plt.get_cmap("Dark2")
    colors = cmap.colors
    colors_l = len(colors)

    for i, vector in enumerate(vectors):
        color = colors[i%colors_l]
        x, y = vector.origin
        plt.quiver(x, y, vector[0], vector[1], scale=1, angles='xy', scale_units='xy', color=color)

    plt.xlim(*lim[0])
    plt.ylim(*lim[1])
    
    plt.grid()

    plt.show()

def grad_to_rad(grad: float)->float:
    """converts grads to radians"""

    return pi * (grad % 360) / 180

def to_polar2d(v: Vector) -> (float, float):
    magnitude = sqrt(sum([i**2 for i in v.coord]))
    angle = atan2(v[1], v[0])

    return magnitude, angle

def to_cartesian2d(magnitude, angle) -> (float, float):
    return magnitude * cos(angle), magnitude * sin(angle)
