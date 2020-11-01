import math

def isNumberPrime(num):
    topNum = math.sqrt(num)
    topNum = math.floor(topNum)
    print(topNum)
    for i in range(topNum-1):
        print("i:", i+2)
        print(num % float(i+2))
        if math.isclose(num % float(i+2)), 0.0):
            return True
    return False

prime = float(input("Enter the number to be tested for being prime: "))
prime = isNumberPrime(prime)
print(prime)