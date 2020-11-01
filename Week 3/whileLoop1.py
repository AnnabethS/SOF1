def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


total = 0
newNum = 1
count = 0
evenCount = 0
while newNum>=0:
    print("Enter a number: ")
    newNum = int(input())
    total += newNum
    count += 1
    if isEven(newNum):
        evenCount += 1
print("Total:", total)
print("Average:", total/count)
print("Even Numbers Entered:", evenCount)