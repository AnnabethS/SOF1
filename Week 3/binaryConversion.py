import math

bigNum = int(input("Enter an integer to be converted to binary... "))
binaryString = ""
while True:
    if bigNum==1:
        binaryString = binaryString+"1"
        break
    else:
        remainder = (bigNum % 2)
        binaryString = binaryString+str(remainder)
        bigNum = bigNum // 2
binaryString = binaryString[::-1]
print(binaryString)