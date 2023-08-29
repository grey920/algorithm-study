def func(items):
    if not items:
        return []

    mapData = {}

    for item in items:
        newItem = ''.join(sorted(item))

        if newItem in mapData:
            mapData[newItem].append(item)
            mapData[newItem].sort()
        else:
            mapData[newItem] = [item]

    answer = list(mapData.values())
    print(answer)
    return answer

words = func(["eat", "tea", "tan", "ate", "nat", "bat"])
result = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]

print( words == result)