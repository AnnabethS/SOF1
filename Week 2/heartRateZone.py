age = int(input("Enter your age: "))
rate = int(input("Enter your heart rate: "))
maxRate = 208 - (0.7*age)
print("Max Rate:", maxRate)
print("Training Zone: ")
if rate<0.5*maxRate:
    print("Couch Potato")
elif rate<0.7*maxRate:
    print("Aerobic Training")
elif rate<0.9*maxRate:
    print("Threshold Training")
else:
    print("Interval Training")
