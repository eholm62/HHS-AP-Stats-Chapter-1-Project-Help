# takes in an array and an index as a float or int,
# and returns the value of the array at that index
# where a non-integer value represents a weighted average
# of the closest two values based on how close the float is
# to each of those indicies
def getWeightedValueAt(i, arr):
    if i < 0:
        i = len(arr) + i
    if i % 1 == 0:
        return arr[int(i)]
    return arr[int(i)] * (i % 1) + arr[int(i) + 1] * (1 - i % 1)

# returns the five number summmary given a list of values
def getFiveNumSummary(arr):
    arr = arr.copy()
    arr.sort()
    
    if len(arr) % 2 != 0:
        posMedian = (len(arr) + 1) // 2 - 1
        posQ1 = (posMedian) / 2
        posQ3 = -posQ1 - 1
    else:
        posMedian = (len(arr) + 1) / 2 - 1
        posQ1 = (int(posMedian)) / 2
        posQ3 = -posQ1 - 1
    
    q1 = getWeightedValueAt(posQ1, arr)
    median = getWeightedValueAt(posMedian, arr)
    q3 = getWeightedValueAt(posQ3, arr)
    iqr = q3 - q1
    
    i = 0
    while q1 - 1.5 * iqr > arr[i]:
        i += 1
    posMin = i

    i = -1
    while arr[i] > q3 + 1.5 * iqr:
        i -= 1
    posMax = i
    
    return (
        arr[posMin],
        q1,
        median,
        q3,
        arr[posMax]
    )

# returns a boolean representing whether or not x is 
# an outlier given the five number summary, using
# the 1.5 * IQR method
def isOutlier(x, fiveNumSummary):
    iqr = (fiveNumSummary[3] - fiveNumSummary[1])
    if x < fiveNumSummary[1] - 1.5 * iqr:
        return True
    elif x > fiveNumSummary[3] + 1.5 * iqr:
        return True
    return False

def getMean(arr):
    return sum(arr) / len(arr)