class Vector:
    def __init__(self, data = []):
        self._vector = data.copy()

    def __str__(self):
        if self.dim()==0:
            return "<>"
        outputString = "<"
        for i in self._vector:
            outputString = outputString + f"{float(i)}, "
        outputString = outputString[:len(outputString)-2] + ">"
        return outputString

    def dim(self):
        return len(self._vector)

    def get(self, index):
        return self._vector[index]
    
    def set(self, index, value):
        self._vector[index] = value
        return

    def scalar_product(self, scalar):
        newVectorData = []
        for i in self._vector:
            newVectorData.append(i*scalar)
        return Vector(newVectorData)

    def add(self, other_vector):
        if type(other_vector)!=type(self):
            raise TypeError
        elif other_vector.dim() != self.dim():
            raise ValueError
        newVectorData = []
        for i in range(self.dim()):
            newVectorData.append(other_vector.get(i)+self.get(i))
        return Vector(newVectorData)

    def equals(self, other_vector):
        if type(other_vector)!=type(self):
            raise TypeError
        elif other_vector.dim() != self.dim():
            return False
        for i in range(self.dim()):
            if other_vector.get(i)!=self.get(i):
                return False
        return True


x = Vector([0, 2, 3])
print(x)
print(x.dim())