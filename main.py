import csv
import numpy as np
import statistics

import mystats

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

fiveNum2020 = mystats.getFiveNumSummary(data2020)
fiveNum2024 = mystats.getFiveNumSummary(data2024)

filteredSample2020 = list(filter(lambda x: not mystats.isOutlier(x, fiveNum2020), sample2020))
filteredSample2024 = list(filter(lambda x: not mystats.isOutlier(x, fiveNum2024), sample2024))

filteredSample2020.sort()
filteredSample2024.sort()

filteredFiveNum2020 = mystats.getFiveNumSummary(sample2020)
filteredFiveNum2024 = mystats.getFiveNumSummary(sample2024)

mean2020 = mystats.getMean(filteredSample2020)
mean2024 = mystats.getMean(filteredSample2024)

mode2020 = statistics.mode(filteredSample2020)
mode2024 = statistics.mode(filteredSample2024)

stdev2020 = statistics.stdev(filteredSample2020)
stdev2024 = statistics.stdev(filteredSample2024)

with open("processed_data.csv", "w") as dataFile:
    for dataPoint in filteredSample2020:
        dataFile.write(str(dataPoint) + ", ")
    dataFile.write("\n")

    for dataPoint in filteredSample2024:
        dataFile.write(str(dataPoint) + ", ")
    dataFile.write("\n")


print("2020 Filtered")
print("Five Number Summary: " + str(filteredFiveNum2020))
print("Mean: " + str(mean2020))
print("Standard Deviation: " + str(stdev2020))
print("Karl Pearson Skewness Coefficient: " + str(3 * (mean2020 - filteredFiveNum2020[2]) / stdev2020))
print("Most Extreme Outlier: " + str(filteredSample2020[-1]))


print()

print("2024 Filtered")
print("Five Number Summary: " + str(filteredFiveNum2024))
print("Mean: " + str(mean2024))
print("Standard Deviation: " + str(stdev2024))
print("Karl Pearson Skewness Coefficient: " + str(3 * (mean2024 - filteredFiveNum2024[2]) / stdev2024))
print("Most Extreme Outlier: " + str(filteredSample2024[-1]))

print()

print("2020 UnFiltered")
print("Five Number Summary: " + str(fiveNum2020))
print("Most Extreme Outlier: " + str(data2020[-1]))


print()

print("2024 UnFiltered")
print("Five Number Summary: " + str(fiveNum2024))
print("Most Extreme Outlier: " + str(data2024[-1]))