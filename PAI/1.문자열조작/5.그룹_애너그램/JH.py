from functools import reduce
from collections import OrderedDict

from typing import List


def anagram(text_list: List[str]) -> List[List[str]]:
    text_to_sorted_dict = reduce(reducer, text_list, OrderedDict())

    return [sorted(text_list) for text_list in text_to_sorted_dict.values()]


def reducer(dictionary, current):
    sorted_current = ''.join(sorted(current))

    if sorted_current in dictionary:
        dictionary[sorted_current].append(current)
        return dictionary

    dictionary[sorted_current] = [current]
    return dictionary


print(anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
