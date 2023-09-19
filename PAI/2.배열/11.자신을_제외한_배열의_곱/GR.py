from functools import reduce


def func(data):
    answer = []
    for i, item in enumerate(data):
        newList = data[:i] + data[i + 1:]
        answer.append(reduce(lambda x, y: x * y, newList))

    return answer

print(func([1,2,3,4]))


