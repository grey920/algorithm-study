def func(list):
    digList = []
    letList = []
    strMap = {}
    answer = []

    for i in list:
        if i.startswith("dig"):
            digList.append(i)
        else:
            letList.append(i)
            strMap[i.split(' ', 1)[1]] = len(letList) - 1

    strMap = {k: v for k, v in sorted(strMap.items())}

    for key, value in strMap.items() :
        answer.append(letList[value])

    return answer + digList

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero", "let4 art can zero"]
result = ["let1 art can", "let4 art can zero", "let3 art zero","let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

print(func(logs) == result)