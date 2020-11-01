print("Input your string:")
userString = input()
print(userString.replace(" ", ""))
string2 = userString.title()
string2 = string2.replace(" ", "")
print(string2)
capitalsPos = []
substrings = []
for i in range(len(string2)):
    if string2[i].isupper():
        capitalsPos.append(i)
for i in range(len(capitalsPos)):
    if i+1>=len(capitalsPos):
        substrings.append(string2[capitalsPos[i]:len(string2)])
    else:
        substrings.append(string2[capitalsPos[i]:capitalsPos[i+1]])
print(substrings)