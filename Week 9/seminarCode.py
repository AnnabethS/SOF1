import math

def voronoiDiagram_iter(matrix, seeds):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            closest_seed = [-1, -1]
            for k in range(len(seeds)):
                this_seed = [k, findDistance((i, j), seeds[k])]
                if this_seed[1]<closest_seed[1]:
                    closest_seed = this_seed.copy()
            matrix[closest_seed[0]][closest_seed[1]] = closest_seed[k]
    return matrix


def findDistance(pos1, pos2):
    xdist = math.fabs(pos1[0] - pos2[0])
    ydist = math.fabs(pos1[1] - pos2[1])
    if xdist==0 and ydist==0:
        return 0
    else:
        return math.sqrt(((xdist)^2) + ((ydist)^2))