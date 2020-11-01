print("Input your number:")
number = int(input())
total = 0
for i in range(number):
    total += (i+1)
print("Sum of the first", number, "Natural Number(s):", total) #not including 0
for i in range(10):
    print(number, "*", (i+1), "=", number*(i+1))
total = 1
for i in range(number):
    total = total*(i+1)
print("Factorial of your number is:", total)