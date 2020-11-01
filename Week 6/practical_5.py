import string

sample_text = (" As Python s creator, I'd like to say a few words about its "+
              "origins adding a bit of personal philosophy. "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas. My office, "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus.  ")

######################### EXERCISE 1 ##########################################

def split_text(text, seperators=" "):
    if text=="":
        return []
    output = []
    prevDelim = -1
    for i in range(len(text)):
        if text[i] in seperators:
            if prevDelim!= i-1:
                output.append(text[prevDelim+1:i])
            prevDelim = i
        elif i == len(text)-1:
            if text[prevDelim+1:i]!="":
                output.append(text[prevDelim+1:i+1])
    return output


######################### EXERCISE 2 ##########################################

def get_words_frequencies(text):
    output = {}
    seperators = string.punctuation + " "
    prevDelim = -1
    for i in range(len(text)):
        if text[i] in seperators:
            if prevDelim!= i-1:
                oldVal = output.get((text[prevDelim+1:i]).lower(), 0)
                output[(text[prevDelim+1:i]).lower()] = oldVal + 1
            prevDelim = i
        elif i == len(text)-1:
            if text[prevDelim+1:i]!="":
                oldVal = output.get((text[prevDelim+1:i]).lower(), 0)
                output[(text[prevDelim+1:i+1]).lower()] = oldVal + 1
    return output


######################### EXERCISE 3 ##########################################

def flatten(list_2D):
    outputList = []
    for i in list_2D:
        for j in i:
            outputList.append(j)
    return outputList


######################### EXERCISE 4 ##########################################

def rasterise(list_1D, width):
    if width<1:
        return None
    if (len(list_1D) % width) != 0:
        return None
    outputList = []
    for i in range(len(list_1D) // width):
        tempList = []
        for j in range(width):
            tempList.append(list_1D[i*width + j])
        outputList.append(tempList)
    return outputList
