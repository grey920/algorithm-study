import unittest
# This is a sample Python script.
import collections
import re
from typing import Deque, List

# 리스트 -> O(n제곱)
def valid_palindrome_list(inputVal):
    strs = []
    for char in inputVal:
        # isalnum() -> 영소문자 구분
        if char.isalnum():
            strs.append(char.lower())

    print(strs)

    # while -> pop(0) -> O(n제곱)
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# 데크 자료형을 이용한 최적화
def valid_palindrome_deque(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum:
            strs.append(char.lower())

    print(strs)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

        return True

# 슬라이싱 사용 ( 알고리즘 X )
def valid_palindrome_slicing(s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)
    print(s)

    return s == s[::-1]


if __name__ == '__main__':
    # 리스트
    result1 = valid_palindrome_list("A man, a plan, a canal: Panama")
    result2 = valid_palindrome_deque("A man, a plan, a canal: Panama")
    result3 = valid_palindrome_slicing("A man, a plan, a canal: Panama")
    print("result1 = ", result1)
    print("result2 = ", result2)
    print("result3 = ", result3)
