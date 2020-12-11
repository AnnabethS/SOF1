import csv
#EXCERCISE 1

def readPrecipitationFromFile(fileName):
    outputList = []
    f = open(fileName, "r")
    outputList = f.readlines()
    f.close()
    outputList.pop(0)
    for i in range(len(outputList)):
        temp = outputList[i].split(",")
        temp[0] = int(temp[0])
        temp[1] = float(temp[1])
        outputList[i] = temp
    return outputList

def minimumPrecipitation(p_list):
    currentMin = [0, 999999999.99999]
    for i in p_list:
        if i[1]<currentMin[1]:
            currentMin = i
    return currentMin

def maximumPrecipitation(p_list):
    currentMax = [0, 0.0]
    for i in p_list:
        if i[1]>currentMax[1]:
            currentMax = i
    return currentMax

def averagePrecipitation(p_list):
    total = 0
    count = 0
    for i in p_list:
        total += i[1]
        count += 1
    return (total / count)

#EXCERCISE 2

def collate_rainfall(inputFiles, outputFile):
    all_data = []
    outputString = ""
    for i in inputFiles:
        all_data.append(readPrecipitationFromFile(i))
    numFiles = len(all_data)
    for i in range(len(all_data[0])):
        row = str(all_data[0][i][0])
        for j in range(numFiles):
            row += "," + str(all_data[j][i][1])
        row += "\n"
        outputString += row
    f = open(outputFile, "w")
    f.write(outputString)
    f.close()




# p_list = readPrecipitationFromFile("Week 10\precipitations-Europe.txt")

# minRain = minimumPrecipitation(p_list)
# maxRain = maximumPrecipitation(p_list)

# print(f"""MINIMUM RAIN: {minRain[1]}ml in the year {minRain[0]},
# MAXIMUM RAIN: {maxRain[1]}ml in the year {maxRain[0]}
# AVERAGE RAIN: {averagePrecipitation(p_list)}ml """)

collate_rainfall(["Week 10\precipitations-Europe.txt",
"Week 10\precipitations-NAmerica.txt",
"Week 10\precipitations-world.txt"],
"precipitations-records.txt")


#EXCERCISE 3

def read_aberporth_data():
    FILENAME = "Week 10/aberporth_meteorological_data.txt"
    f = open(FILENAME)
    data = f.readlines()
    f.close()
    data.pop(0)
    data.pop(0)
    outputData = []
    for i in range(len(data)//12):
        outputData.append([])
    year_index = -1
    current_year = 0
    for line in data:
        dataList = line.split(",")
        dataList[0] = int(dataList[0])
        dataList[1] = int(dataList[1])
        dataList[2] = float(dataList[2])
        dataList[3] = float(dataList[3])
        dataList[4] = int(dataList[4])
        dataList[5] = float(dataList[5])
        dataList[6] = float(dataList[6])
        if current_year!=dataList[0]:
            year_index+=1
            current_year = dataList[0]
        outputData[year_index].append(dataList)
    return outputData
    #format of outputData = [year_index][month_index(0-11)][data_index]
    #data_index: 0=year ¦ 1=month ¦ 2=max temp ¦ 3=min temp ¦ 4=days of airfrost ¦ 5=rain(mm) ¦ 6=sun(hours)
    
def get_total_aberporth_data(full_data, data_index, year_index):
    total = 0
    for i in range(12):
        total += full_data[year_index][i][data_index]
    return total

def output_csv_data(full_data, filename):
    outputData = [["Year", "Days of Air Frost (af)", "Total Rainfall For Year(mm)", "Total Sunshine For Year (hrs)"]]
    for i in range(len(full_data)):
        year_data = [full_data[i][0][0], #year
        get_total_aberporth_data(full_data, 4, i),
        get_total_aberporth_data(full_data, 5, i),
        get_total_aberporth_data(full_data, 6, i)]
        outputData.append(year_data)
    f = open(filename, "w")
    writer = csv.writer(f)
    for i in outputData:
        writer.writerow(i)
    f.close()

aberporth_data = read_aberporth_data()
output_csv_data(aberporth_data, "Week 10/csvtest.csv")

