def getLine():
    line = []
    print("Enter 4 numbers from 0..4 inclusive seperated by whitespace")
    userInput = input()
    line = userInput.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    return line

def getGrid():
    grid = []
    line = []
    for i in range(4):
        line = getLine()
        grid.append(line)
    return grid

def outputLine(line):
    print("|"+displayNum(line[0])+"|"+displayNum(line[1])+"|"+displayNum(line[2])+"|"+displayNum(line[3])+"|")

def outputGrid(grid):
    for i in range(4):
        print("+-+-+-+-+")
        outputLine(grid[i])
    print("+-+-+-+-+")

def displayNum(num):
    if num==0:
        return " "
    else:
        return str(num)


grid = getGrid()

outputGrid(grid)
