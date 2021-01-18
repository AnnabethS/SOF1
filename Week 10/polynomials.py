import math

class Polynomial:
    def __init__(self, coefficients):
        self._coef = coefficients.copy()
        self._size = len(self._coef)

    def eval(self, x):
        total = 0
        for i in range(len(self._coef)):
            total += (math.pow(x, i)) * self._coef[i]
        return total
    
    def getCoef(self, coef):
        if coef>=self._size:
            return 0
        else:
            return self._coef[coef]

    def add(self, other):
        newPolyCoef = []
        if self._size == other._size:
            for i in range(self._size):
                newPolyCoef.append(self._coef[i] + other._coef[i])
        elif self._size>other._size:
            for i in range(self._size):
                newPolyCoef.append(self.getCoef(i) + other.getCoef(i))
        else:
            for i in range(other._size):
                newPolyCoef.append(self.getCoef(i) + other.getCoef(i))
        return Polynomial(newPolyCoef)

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self.add(other)
            
    

test = Polynomial([5, 0, 2, 0, 1])
test2= Polynomial([4, 1, 3, 0, 0, 5])
print(test.eval(1))
print(test.eval(0))
test += test2
print(test._coef)