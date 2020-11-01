def largestSubList(list1):
    highestSum = 0
    highestSumIndex = -1
    highestSumLength = -1
    for i in range(len(list1)):
        for j in range((len(list1)-1)-i):
            currtotal = 0
            print(i,j)
            for k in range(i, (i+j)):
                currtotal = currtotal + list1[k]
            if currtotal > highestSum:
                highestSum = currtotal
                highestSumIndex = i
                highestSumLength = j
    return highestSum, highestSumIndex, highestSumLength



def largestSubRectangle(list1):
    largestSum = -1 #use to check the rectangles and keep track of the one with the biggest sum
    largestSumIndex = [-1, -1]
    largestSumSize = [-1, -1]
    listWidth = len(list1)
    listHeight = len(list1[0])
    for i in range(listWidth):
        for j in range(listHeight):
            for xLen in range(listWidth - i):
                for yLen in range(listHeight - j):
                    print(i, j, xLen, yLen)
                    currentSum = 0
                    if xLen==0 and yLen!=0:
                        for y in range(yLen):
                            currentSum = currentSum + list1[i][j+y]
                    elif xLen!=0 and yLen==0:
                        for x in range(xLen):
                            currentSum = currentSum + list1[i+x][j]
                    elif xLen==0 and yLen==0:
                        currentSum = list1[i][j]
                    else:
                        for x in range(xLen+1):
                            for y in range(yLen+1):
                                currentSum = currentSum + list1[i+x][j+y]
                    if currentSum>largestSum:
                        largestSum = currentSum
                        largestSumIndex = [i,j]
                        largestSumSize = [xLen+1, yLen+1]
    return largestSum, largestSumIndex, largestSumSize


print(largestSubList([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

print(largestSubRectangle([
    [6, -5, -7, 4, -4],
    [-9, 3, -6, 5, 2],
    [-10, 4, 7, -6, 3],
    [-8, 9, -3, 3, -7]]))