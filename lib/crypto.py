from abc import ABCMeta, abstractmethod
from lib.la import Vector
from lib.num import gen_primes

import math
import random

class Crypto(metaclass=ABCMeta):
    @abstractmethod
    def encrypt(self, value: int) -> int:
        pass

class RSA(Crypto):
    """Naive way of implementation of RSA"""
    
    def __init__(self, p1, p2):
        self.n = p1 * p2
        self.z = (p1 - 1) * (p2 - 1)
        
        primes_to_z = list(gen_primes(self.z))
        # public_key should be also checked if it's divisor of z
        self.public_key = random.choice(primes_to_z)
        self.private_key = self.__find_private_key(self.public_key, self.z)

    def __find_private_key(self, pub, phi)->int:
        for i in range(1, phi):
            x = 1 + i * phi
            if x % pub == 0:
                private = x // pub
                break

        return private

    def encrypt(self, value: int) -> int:
        return value ** self.public_key % self.n

    def decrypt(self, value: int) -> int:
        return value ** self.private_key % self.n

class EllipticCurve(Crypto):
    """Creates an instance of elliptic curve and provides the necessary calculations for ECC"""

    def __init__(self, a, b):
        """Provide the constants for y^2 = x^3 + ax + b"""
        self.a = a
        self.b = b
        self.private = random.randint(100, 200)

    def encrypt(self, value: int) -> int:
        pass

    def get_y_by_x(self, x: float) -> (float, float):
        top = math.sqrt(x**3 + self.a * x + self.b)

        return (top, -top)

    def line(self, point1: Vector, point2: Vector) -> (float, float):
        """Calculates either tangent or secant of"""

        if point1 == point2:
            return self.__calculate_tangent(point1)
        else:
            return self.__calculate_secant(point1, point2)

    def nextPoint(self, point1: Vector, point2: Vector) -> Vector:
        pass

    def __calculate_tangent(self, point: Vector) -> (float, float):
        x, y = point
        slop = (3*x**2 + self.a) / (2*y)
        shift = y - slop*x

        return (slop, shift)

    def __calculate_secant(self, point1: Vector, point2: Vector) -> (float, float):
        x1, y1 = point1
        x2, y2 = point2

        slop = (y2 - y1)/(x2 - x1)
        shift = y1 - slop*x1

        return (slop, shift)
