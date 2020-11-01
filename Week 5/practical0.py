#EXCERCISE 2
def display_dict(userDict):
    for i in userDict:
        print(i, "--->", userDict[i])


#EXCERCISE 1
months = {1:"january", 2:"feburary", 3:"march", 4:"april", 5:"may", 6:"june", 7:"july",
    8:"august", 9:"september", 10:"october", 11:"november", 12:"december"}

romanNumbers = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

elements = {"H":"Hydrogen", "He":"Helium", "Li":"Lithium", "Be":"Beryllium", "B":"Boron",
    "C":"Carbon", "N":"Nitrogen"}

roman = {}
roman[10000] = "T"
roman[1000] = "M"
roman[500] = "D"
roman[100] = "K"
roman[50] = "L"
roman[10] = "X"
roman[5] = "V"
roman[1] = "I"
print(roman)

roman[100] = "C"

print(roman)

roman.pop(10000)

display_dict(roman)

#EXCERCISE 2

def concat_dict(dict1, dict2):
    outputDict = dict1
    for i in dict2:
        if dict1.get(i)!=None:
            outputDict[i] = [dict1[i], dict2[i]]
        else:
            outputDict[i] = dict2[i]
    return outputDict

print(concat_dict({"one":1, "two":2, "three":3}, {"three":"bruh", "four":4, "five":5}))

#EXCERCISE 3

def map_list(list1, list2):
    outputDict = {}
    set1 = set(list1)
    if len(set1)!=len(list1):
        print("DUPLICATES IN KEYS LIST, EXITING...")
        return None
    for i in range(len(list1)):
        outputDict[list1[i]] = list2[i]
    return outputDict

print(map_list([1, 2, 3, 5, 5], [6, 2, 3, 1, 2]))


#EXCERCISE 4

def reverse_dict(inputDict):
    outputDict = {}
    set1 = set(inputDict)
    if len(set1)!=len(inputDict):
        print("DUPLICATES IN KEYS, EXITING...")
        return None
    for i in inputDict:
        outputDict[inputDict[i]] = i
    return outputDict

print(reverse_dict({"one":1, "three":3, "five":5, "one":1}))