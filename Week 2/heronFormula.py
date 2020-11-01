import math
sideA = float(input("Input side A: "))
sideB = float(input("Input side B: "))
sideC = float(input("Input side C: "))
semiPerimeter = (sideA + sideB + sideC) / 2
area = math.sqrt(semiPerimeter * (semiPerimeter - sideA)* (semiPerimeter - sideB)* (semiPerimeter - sideC))
print("The Area of the triangle is", area)