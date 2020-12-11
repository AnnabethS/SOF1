import math

class Polynomial:
    def __init__(self, coefficients):
        self._coef = coefficients.copy()

    def eval(self, x):
        total = 0
        for i in range(len(self._coef)):
            total += (math.pow(x, i)) * self._coef[i]
        return total

    def add(self, other):
        
    

test = Polynomial([5, 0, 2, 0, 1])
print(test.eval(1))
print(test.eval(0))