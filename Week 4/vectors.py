def scalar_product(scalar, vector):
    for i in range(len(vector)):
        vector[i] = vector[i] * scalar
    return vector

def vector_addition(vector1, vector2):
    if len(vector1)!=len(vector2):
        print("VECTORS DO NOT HAVE THE SAME DIMENSION, EXITING...")
        return None
    else:
        totalVector = []
        for i in range(len(vector1)):
            totalVector.append(vector1[i] + vector2[i])
        return totalVector

print(scalar_product(3, [1, 2, 3]))

print(vector_addition([4, 5, 6], [6, 5, 4]))

print(vector_addition([1, 2, 3], [1, 2]))