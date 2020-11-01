letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"
    , "t", "u", "v", "w", "x", "y", "z"]
shiftAmount = 3

def encode(userString):
    newString = ""
    for i in range(len(userString)):
        num = letterToNum(userString[i])
        num = num+shiftAmount
        if num>25:
            num = num - 26
        newString = newString + (numToLetter(num))
    return newString


def decode(userString):
    newString = ""
    for i in range(len(userString)):
        num = letterToNum(userString[i])
        num = num-shiftAmount
        if num<0:
            num = 26 + num
        newString = newString + (numToLetter(num))
    return newString

def letterToNum(letter):
    letter = letter.lower()
    for i in range(len(letters)):
        if letters[i]==letter:
            return i

def numToLetter(num):
    return letters[num]

while True:
    print("""What would you like to do?
    1. Encode
    2. Decode
    3. Encode-Decode
    4. Exit""")

    choice = input()
    if choice=="1":
        print("Enter your string...")
        userString = input()
        print(encode(userString))
    elif choice=="2":
        print("Enter your string...")
        userString = input()
        print(decode(userString))
    elif choice=="3":
        print("Enter your string...")
        userString = input()
        encoded = encode(userString)
        print(encoded)
        print(decode(encoded))
    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("Invalid choice selection, select 1-4 \n ----------------- \n")
