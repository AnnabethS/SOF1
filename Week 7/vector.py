class Vector:
    def __init__(self, *data):
        if len(data)==0:
            self._vector = []
            return
        self._vector = []
        if type(data[0])==list:
            self._vector = data[0].copy()
        else:
            for i in data:
                if type(i)==int:
                    self._vector.append(i)
                else:
                    raise TypeError

    def __str__(self):
        if self.dim()==0:
            return "<>"
        outputString = "<"
        for i in self._vector:
            outputString = outputString + f"{float(i)}, "
        outputString = outputString[:len(outputString)-2] + ">"
        return outputString

    def __eq__(self, other_vector):
        return self.equals(other_vector)

    def __ne__(self, other_vector):
        return not self.equals(other_vector)

    def __add__(self, other_vector):
        return self.add(other_vector)

    def __mul__(self, scalar):
        raise TypeError
    
    def __rmul__(self, scalar):
        if type(scalar)==int:
            return self.scalar_product(scalar)

    def __iadd__(self, other_vector):
        return self.add(other_vector)

    def __imul__(self, scalar):
        return self.scalar_product(scalar)    

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, data):
        self.set(index, data)
        return

    def dim(self):
        return len(self._vector)

    def get(self, index):
        return self._vector[index]
    
    def set(self, index, value):
        self._vector[index] = value
        return

    def scalar_product(self, scalar):
        if type(scalar)!=int:
            raise TypeError
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
        if type(other_vector)==list:
            for i in range(self.dim()):
                if other_vector[i]!=self.get(i):
                    return False
        elif type(other_vector)!=type(self):
            raise TypeError
        elif other_vector.dim() != self.dim():
            return False
        else:
            for i in range(self.dim()):
                if other_vector.get(i)!=self.get(i):
                    return False
            return True


x = Vector([0, 2, 3])
print(x)
print(x.dim())
