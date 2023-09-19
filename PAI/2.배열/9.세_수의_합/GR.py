from itertools import *
def func(itemList):
    if not list:
        return []

    newList = list(permutations(itemList, 3))

    answer = set()

    for item in newList:
        if sum(item) == 0:
            answer.add(tuple(sorted(item)))
    answer = [list(item) for item in answer]

    return answer

print(func([-1, 0, 1, 2, -1, -4]))


