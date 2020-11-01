print("Input your string: ")
userString = input()
userString = userString.replace(" ", "")
userString = userString.replace(",", "")
userString = userString.replace("'", "")
userString = userString.replace("!", "")
userString = userString.replace(".", "")
print(userString)
checkAmount = len(userString) // 2
strLen = len(userString)
palindrome = True
for i in range(checkAmount):
    if(userString[i]!=userString[strLen-1-i]):
        palindrome = False

print(palindrome)