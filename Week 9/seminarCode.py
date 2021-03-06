import math
import random
from PIL import Image


def imageOutput(matrix, seeds):
    colours = []
    for i in range(len(seeds)):
        colours.append((
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        ))
    size = len(matrix)
    outputImage = Image.new("RGB", (size, size), "black")
    pixels = outputImage.load()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            pixels[j, i] = colours[matrix[j][i]]
    for i in seeds:
        pixels[i[1], i[0]] = (0,0,0)
    outputImage.save("test.png")

def voronoiDiagram_iter(matrix, seeds):
    matrixSize = len(matrix)
    for i in range(matrixSize):
        for j in range(matrixSize):
            closest_seed = [-1, 1000]
            for k in range(len(seeds)):
                this_seed = [k, findDistance((i, j), seeds[k])]
                if this_seed[1] < closest_seed[1]:
                    closest_seed = this_seed.copy()
            matrix[j][i] = closest_seed[0]
    return matrix

def findDistance(pos1, pos2):
    xdist = math.fabs(pos1[0] - pos2[0])
    ydist = math.fabs(pos1[1] - pos2[1])
    if xdist==0 and ydist==0:
        return 0
    else:
        return math.sqrt((math.pow(xdist, 2)) + (math.pow(ydist, 2)))

def blankMatrix(size):
    row = []
    matrix = []
    for i in range(size):
        row.append(-1)
    for i in range(size):
        matrix.append(row.copy())
    return matrix

def matrixOutput(matrix, seeds=()):
    for i in range(len(matrix)):
        rowString = ""
        for j in range(len(matrix[i])):
            rowString += str(matrix[i][j]) + " "
        print(rowString) 

def randomSeeds(size, amount):
    seeds = []
    for i in range(amount):
        seeds.append((random.randint(0,size-1), random.randint(0,size-1)))
    return seeds

def voronoiDiagram_rec(matrix, seeds, diagonalNeighbours):
    def finder(matrix, seeds, diagonalNeighbours): #diagonalNeighbours = false; its a 4-neighbourhood, otherwise its an 8 neighbourhood
        matrixSize = len(matrix)
        if matrixIsDone(matrix, -1):
            return matrix
        else:
            seedAmount = len(seeds)
            for i in range(seedAmount):
                x = seeds[0][0][0]
                y = seeds[0][0][1]
                seedID = seeds[0][1]
                modifiers = [[0,1], [0,-1], [1,0], [-1,0]]
                for i in modifiers:
                    if isInRangeOfMatrix(matrixSize, x+i[0], y+i[1]):
                        if matrix[y+i[1]][x+i[0]]==-1:
                            seeds.append([(x+i[0], y+i[1]), seedID])
                            matrix[y+i[1]][x+i[0]] = seedID

                if diagonalNeighbours:
                    diagModifiers = [[1,1], [1,-1], [-1,1], [-1,-1]]
                    for i in diagModifiers:
                        if isInRangeOfMatrix(matrixSize, x+i[0], y+i[1]):
                            if matrix[y+i[1]][x+i[0]]==-1:
                                seeds.append([(x+i[0], y+i[1]), seedID])
                                matrix[y+i[1]][x+i[0]] = seedID
                seeds.pop(0)
            return finder(matrix, seeds, diagonalNeighbours)
    formattedSeeds = []
    for i in range(len(seeds)):
        formattedSeeds.append([seeds[i], i])
    return finder(matrix, formattedSeeds, diagonalNeighbours)


def isInRangeOfMatrix(size, x, y):
    if x>=0 and x<size and y>=0 and y<size:
        return True
    else:
        return False


def matrixIsDone(matrix, emptyChar):
    for i in matrix:
        if emptyChar in i:
            return False
    return True

def imageNeighbourhoods(matrix, diagonalNeighbours):
    currentNeighbourhood = 2
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                matrix = floodFill(matrix, currentNeighbourhood, (i,j), diagonalNeighbours)
                currentNeighbourhood += 1
    return matrix


def floodFill(matrix, replacement, start, diagonalNeighbours):
    possibleNodes = [start]
    modifiers = []
    if diagonalNeighbours:
        modifiers = [
            [0,1], [0,-1], 
            [1,0], [1,1], [1,-1], 
            [-1,1], [-1,0], [-1,-1]]
    else:
        modifiers = [
            [0,1],[0,-1],
            [1,0],[-1,0]
        ]
    while len(possibleNodes) > 0:
        for i in modifiers:
            if isInRangeOfMatrix(len(matrix), possibleNodes[0][0]+i[0], possibleNodes[0][1]+i[1]):
                if matrix[possibleNodes[0][0]+i[0]][possibleNodes[0][1]+i[1]]==1:
                    matrix[possibleNodes[0][0]+i[0]][possibleNodes[0][1]+i[1]] = replacement
                    possibleNodes.append((possibleNodes[0][0]+i[0], possibleNodes[0][1]+i[1]))
        possibleNodes.pop(0)
    return matrix
        

# matrixOutput(imageNeighbourhoods([
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 1, 0, 0],
#     [1, 1, 1, 0, 1, 1, 1, 0],
#     [1, 0, 1, 0, 0, 1, 1, 0],
#     [1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 1, 1],
# ], False))

MATRIX_SIZE = 50   
SEEDS_AMOUNT = 3
seeds = randomSeeds(MATRIX_SIZE, SEEDS_AMOUNT)
complete_matrix = voronoiDiagram_rec(blankMatrix(MATRIX_SIZE), seeds, True)
print("matrix processed")
matrixOutput(complete_matrix, seeds)
print("image processed + output")