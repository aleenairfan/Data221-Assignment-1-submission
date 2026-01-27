# Nested Dictionary from Strings

def buildStringDictionary(stringList):
    resultDictionary = {}

    for word in stringList:
        stringLength = len(word)
        parity = "even" if stringLength % 2 == 0 else "odd"

        resultDictionary[word] = {
            "length": stringLength,
            "parity": parity
        }

    return resultDictionary


# Example test
words = ["data", "science"]
print(buildStringDictionary(words))
