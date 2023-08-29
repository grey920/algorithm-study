import re
from functools import reduce


def frequent(paragraph: str) -> str:
    regex = re.compile('(\w+)')

    text_list = regex.findall(paragraph.lower())

    count_dictionary = reduce(reducer, text_list, {})

    return f'"{max(count_dictionary, key=count_dictionary.get)}"'


def reducer(dictionary, current):
    if current in banned_dictionary:
        return dictionary

    if current not in dictionary:
        dictionary[current] = 0
    dictionary[current] += 1
    return dictionary


input_paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# banned_dictionary 를 만드는데는, banned의 length에 대한 o(n)
banned_dictionary = {string: 1 for string in banned}

print(frequent(input_paragraph))
