def sum_all(n):
    total = 0
    if n<=0:
        return -1
    for i in range(n):
        total = total + i
    return total

def mul_table(n):
    if n<0:
        print("Number cannot be <0 for multiplication tables function")
    for i in range(10):
        print(n, "*", i+1, "=", n*(i+1))

def factorial(n):
    if n<0:
        return -1
    total = 1
    for i in range(n):
        total = total * (i+1)
    return total


num = int(input("Enter your number: "))
print("The sum of the first", num, "natural numbers is:", sum_all(num))
mul_table(num)
print(factorial(num))