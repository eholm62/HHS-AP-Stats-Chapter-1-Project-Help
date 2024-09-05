import csv
import numpy as np

import stats

# must download these files and name them appropiately based on the year
# before use of program
# obtain files from https://survey.stackoverflow.co/

# 6 is the column including the salary data 
nonNumericData2020 = []
data2020 = []
with open("survey_results_public_2020.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            data2020.append(float(row[6])) 
        except:
            nonNumericData2020.append(row[6])


# 21 is the column including the salary data
nonNumericData2024 = []
data2024 = []
with open("survey_results_public_2024.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            data2024.append(float(row[21]))
        except:
            nonNumericData2024.append(row[21])


data2020.sort()
data2024.sort()

sample2020 = np.random.choice(data2020, 10000)
sample2024 = np.random.choice(data2024, 10000)

fiveNum2020 = stats.getFiveNumSummary(data2020)
fiveNum2024 = stats.getFiveNumSummary(data2024)

filteredSample2020 = list(filter(lambda x: not stats.isOutlier(x, fiveNum2020), sample2020))
filteredSample2024 = list(filter(lambda x: not stats.isOutlier(x, fiveNum2024), sample2024))

with open("processed_data.csv", "w") as dataFile:
    for dataPoint in filteredSample2020:
        dataFile.write(str(dataPoint) + ", ")
    dataFile.write("\n")

    for dataPoint in filteredSample2024:
        dataFile.write(str(dataPoint) + ", ")
    dataFile.write("\n")