import collections
import string
from typing import List, Deque, re

# 06. 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팰린드롬 문자열을 출력하라.
# 예제 1
# 입력
palindrome_input = "babad"


# 출력
# "bab"
# 또는
# "aba"


# 데크 자료형을 이용한 최적화
def valid_palindrome_deque(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum:
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

        return True


def palindrome(inputVal: str):
    print("inputVal = ", inputVal)

    strs: Deque = collections.deque()

    resultStr = ""

    # 문자를 하나씩 더하며 출력
    for char in inputVal:
        strs.append(char)
        joinStr = ''.join(strs)

        if len(joinStr) > 1:
            slicing = valid_palindrome_deque(joinStr)
            if slicing:
                if len(joinStr) > 0 and len(joinStr) > len(resultStr):
                    resultStr = joinStr

    print("resultStr = ", resultStr)


if __name__ == '__main__':
    palindrome(palindrome_input)
