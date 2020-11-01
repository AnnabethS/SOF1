def findNumberPairs(list, target):
    pairs = []
    for i in range(len(list)): #loop for finding number 1
        if (i>0 and i>target and target>0):
            break
        for j in range(i, len(list)):
            current = list[i]+list[j]
            if current>target:
                continue
            elif current==target:
                pairs.append([list[i], list[j]])
    print(pairs)

choice = [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

findNumberPairs(choice, 8)