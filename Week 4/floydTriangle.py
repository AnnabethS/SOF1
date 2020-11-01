ROWS = 10

currRow = 1
prevNum = 0

for i in range(ROWS-1):
    line = []
    for j in range(i+1):
        line.append(prevNum+j)
    prevNum = line[len(line)-1] + 1
    print(line)

        