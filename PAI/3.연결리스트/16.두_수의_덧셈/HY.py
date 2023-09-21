import re
from collections import deque


# 16. 두 수의 덧셈
# 역순으로 저장된 연결 리스트의 숫자를 더하라.
#
# 예제 1
# 입력
# (2 -> 4 -> 3) + (5 -> 6 -> 4)


# 출력
# 7 -> 0 -> 8

# ### 설명
# 342 + 465 = 807

#   3 4 2
# + 4 6 5
# --------
#   8 0 7

# (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 리버스 -> (4 <- 6 <- 5) + (3 <- 4 <- 2)

# 숫자를 제외한 모든 문자를 제거
def remove_non_numeric(input_string):
    cleaned_string = re.sub(r'[^0-9]', '', input_string)
    return cleaned_string


# 숫자와 + 기호를 제외한 모든 문자를 제거
def keep_numbers_and_plus(input_string):

    cleaned_string = re.sub(r'[^0-9+]', '', input_string)
    return cleaned_string


def solution(value: str):
    print("start", value)

    # 숫자와 + 기호를 제외한 모든 문자를 제거
    numeric_str = keep_numbers_and_plus(value)
    print("( 예상 243+564 ) numeric_str = ", numeric_str)

    reversed_str = numeric_str[::-1]
    print("( 예상 465+342 ) reversed_str = ", reversed_str)

    numbers_str_list = reversed_str.split("+")
    print("numbers_str_list = ", numbers_str_list)

    sumNum = sum(int(val) for val in numbers_str_list)
    print("sumNum = ", sumNum)

    # 각 자리수를 뒤집은 후, 숫자를 문자열로 변환
    result = "->".join(str(val) for val in str(sumNum)[::-1])

    print("result = ", result)
    print("전체 시간 복잡도는  O(n + m + log(sumNum))")


if __name__ == '__main__':
    input_val = "(2 -> 4 -> 3) + (5 -> 6 -> 4)"

    solution(input_val)
