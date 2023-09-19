def func(nums, target):
    mapData = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in mapData:
            return [mapData[complement], index]

        mapData[num] = index

    return []

print(func([2, 7, 11, 15], 9))