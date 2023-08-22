import unittest
from collections import deque
from typing import List, Any


# 문자열 뒤집기 - 문제..잘못 이해...
def revers_string_deque(val) -> deque[Any]:
    deque_val = deque(val)
    deque_val.reverse()
    return deque_val


# 문제 답
def rever_string(val: List[str]) -> None:
    print(val)
    val.reverse()


input1 = ["h", "e", "l", "l", "o"]
input2 = ["H", "a", "n", "n", "a", "h"]

if __name__ == '__main__':
    rever_string(input1)
    rever_string(input2)

    print("result - 1 = ", input1)
    print("result - 2 = ", input2)
