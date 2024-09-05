import csv

# must download these files and name them properly before use of program
# get files from https://survey.stackoverflow.co/

data2020 = []
with open("survey_results_public_2020.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            data2020.append(float(row[6]))
        except:
            print("Non Numeric Value: " + row[6])


data2024 = []
with open("survey_results_public_2024.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            data2024.append(float(row[21]))
        except:
            print("Non Numeric Value: " + row[21])


print(data2020)
print(data2024)
