from math import pi
import numpy as np
import matplotlib.pyplot as plt

class Vector:
    """Creates a vector"""

    def __init__(self, *coordinates: float):
        self.coord = coordinates

    def __iter__(self):
        return iter(self.coord)

    def __getitem__(self, index: int) -> float:
        return self.coord[index]

    def __str__(self):
        coords = ', '.join(map(str, self.coord))
        return f"({coords})"

    def __add__(self, other):
        point = [a + b for a, b in zip(self.coord, other)]
        return Vector(*point)

def grad_to_rad(grad: float)->float:
    """converts grads to radians"""

    return pi * (grad % 360) / 180

def draw2d(*vectors, figsize=(7, 7)):

    plt.figure(figsize=figsize)

    for vector in vectors:
        plt.quiver(0, 0, vector[0], vector[1], scale=1, angles='xy', scale_units='xy', color="red")

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    plt.grid()

    plt.show()
