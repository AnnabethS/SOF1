import math

def sum_digits(num):
    total = 0
    for i in range(len(num)):
        total = total + int(num[i])

    print("Total:", total)

def pairwise_digits(num1, num2):
    outputString = ""
    if len(num1)<len(num2):
        shortLen = len(num1)
    else:
        shortLen = len(num2)
    for i in range(shortLen):
        if num1[i]==num2[i]:
            outputString = outputString + "1"
        else:
            outputString = outputString + "0"
    print(outputString)

def binaryToDenary(binary):
    total = 0
    length = len(binary)
    for i in range(len(binary)):
        if binary[i]=="1":
            total = total + int(math.pow(2, (length-i)))
    print(total)

choice = input("ENTER NUMBER: ")
if choice!="-1":
    sum_digits(choice)

choice1 = input("ENTER NUM 1: ")
if choice1!="-1":
    choice2 = input("ENTER NUM 2: ")
    pairwise_digits(choice1, choice2)

choice = input("ENTER BINARY STRING: ")
binaryToDenary(choice)