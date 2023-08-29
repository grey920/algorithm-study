import re
def func( item ) :
    listItem = item.split(" ")

    result = {}
    for i in listItem :
        text = re.sub(r'[^a-zA-Z]', '', i.lower())

        if text not in result :
            result[text] = 1
        else :
            result[text] = result[text] + 1

    answer = max(result, key=result.get)
    return answer

print(func("Bob hit a ball, the hit BALL flew far after it was hit."))