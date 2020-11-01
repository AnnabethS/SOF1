def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


print("Enter your series of numbers seperated by a single space each...")
numString = input()
nums = numString.split()
evenNums = []
for i in range(len(nums)):
    nums[i] = int(nums[i])
    if isEven(nums[i]):
        evenNums.append(nums[i])

print("Number of even numbers: ", len(evenNums))
print("Even Numbers: ", evenNums)

nonDupeEvenNumbers = []
for i in range(len(evenNums)):
    if not evenNums[i] in nonDupeEvenNumbers:
        nonDupeEvenNumbers.append(evenNums[i])

print("There are", len(nonDupeEvenNumbers), "non duplicate even numbers")
print(nonDupeEvenNumbers)