def splitString(text, delimiters):
    output = []
    prevDelim = -1
    for i in range(len(text)):
        if text[i] in delimiters:
            if prevDelim!= i-1:
                output.append(text[prevDelim+1:i])
            prevDelim = i
    print(output)

splitString("As Python's creator, I'd like to say a few words about its origins.", ", '.")