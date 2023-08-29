def func(item):
    answer = []
    mapData = {}
    charList = [char for char in item]
    print(charList)

    for startIndex, value1 in enumerate(charList):

        result = []

        for index, value2 in enumerate(charList[startIndex:], start=startIndex):
            result.append(value2)
            if result[0] == value2:
                answer.append(result)
                mapData[''.join(map(str, result))] = len(result)

    if not mapData :
        return []

    maxValue = max(mapData.values())
    maxKeys = [key for key, value in mapData.items() if value == maxValue]

    return maxKeys

result1 = func("babad")
result2 = func("cbbd")

print(result1)  # ["aba", "bab"]
print(result2)  # ["bb"]