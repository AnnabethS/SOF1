letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"
    , "t", "u", "v", "w", "x", "y", "z"]

def encode(userString, shiftAmount):
    newString = ""
    for i in range(len(userString)):
        if userString[i].isalpha():
            num = letterToNum(userString[i])
            num = num+shiftAmount
            if num>25:
                num = num - 26
            newString = newString + (numToLetter(num))
        else:
            newString = newString + userString[i]
    return newString
     

def decode(userString, shiftAmount):
    newString = ""
    for i in range(len(userString)):
        if userString[i].isalpha():
            num = letterToNum(userString[i])
            num = num-shiftAmount
            if num<0:
                num = 26 + num
            newString = newString + (numToLetter(num))
        else:
            newString = newString + userString[i]
    return newString

def letterToNum(letter):
    letter = letter.lower()
    for i in range(len(letters)):
        if letters[i]==letter:
            return i

def numToLetter(num):
    return letters[num]

def bruteForceDecrypt(text):
    for i in range(25):
        print(i, ":", decode(text, i+1))

bruteForceDecrypt("bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc bmtt bpmu bw lw.")

# it was shifted 7 orginally