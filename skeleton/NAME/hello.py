import math
import array
from sys import argv


class Arithmetic:
    def sum (self, a, b):
        return a+b

    def max (self, a, b):
        return (a > b) and a or b

    def square (self, n):
        return n * n;

    def average (self, arr):
        return sum (arr) / len(arr)
