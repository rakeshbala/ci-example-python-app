import numpy as np

class MyMatrix:
    def __init__(self, x, y):
        self.matrix = np.arange(x * y).reshape(x, y)

    def get(self, x, y):
        return self.matrix[x, y]
