# Distribution Analysis

def distributionAnalysis(numbers):
    resultDictionary = {}
    totalCount = len(numbers)

    for value in sorted(set(numbers)):
        countLessOrEqual = sum(1 for n in numbers if n <= value)
        resultDictionary[value] = (countLessOrEqual / totalCount) * 100

    return resultDictionary


# Example test
numbers = [3, 1, 2, 3, 4, 2]
print(distributionAnalysis(numbers))
