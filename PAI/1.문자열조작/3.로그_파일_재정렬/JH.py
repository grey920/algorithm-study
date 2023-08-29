from functools import reduce
import re
from typing import List


def log_sort(log: List[str]) -> List[str]:
    new_list = reduce(reducer, log, {'alp': [], 'num': []})

    new_list['alp'].sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
    return new_list['alp'] + new_list['num']


def reducer(previous, current):
    regex = re.compile('(\w+) ([^0-9])')
    if regex.match(current):
        previous['alp'].append(current)
        return previous
    previous['num'].append(current)
    return previous


print(log_sort(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
