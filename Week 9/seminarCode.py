import math
import random
from PIL import Image

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

# matrixOutput(voronoiDiagram_iter(blankMatrix(100),  randomSeeds(100, 6)))

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
                if isInRangeOfMatrix(matrixSize, x+1, y):
                    if matrix[y][x+1]==-1:
                        seeds.append([(x+1, y), seedID])
                        matrix[y][x+1] = seedID
                if isInRangeOfMatrix(matrixSize, x-1, y):
                    if matrix[y][x-1]==-1:
                        seeds.append([(x-1, y), seedID])
                        matrix[y][x-1] = seedID
                if isInRangeOfMatrix(matrixSize, x, y+1):
                    if matrix[y+1][x]==-1:
                        seeds.append([(x, y+1), seedID])
                        matrix[y+1][x] = seedID
                if isInRangeOfMatrix(matrixSize, x, y-1):
                    if matrix[y-1][x]==-1:
                        seeds.append([(x, y-1), seedID])
                        matrix[y-1][x] = seedID
                if diagonalNeighbours:
                    pass #add the diagonal neighbours too
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

matrixOutput(voronoiDiagram_rec(blankMatrix(10),  randomSeeds(10, 3), False))