import string
from typing import List

# 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등)또한 무시한다.
# 예제 1
# 입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


# 출력
# "ball"

def most_common_word(inputVal: str, bannedList: List[str]):
    print("inputVal", inputVal)
    print("bannedList", bannedList)

    # 문자열에서 구두점 제거
    inputVal = inputVal.translate(str.maketrans('', '', string.punctuation))
    print("1)구두점 제거", inputVal)

    newStr = ""

    # 금지된 단어 제거
    for forbidden in bannedList:
        newStr = inputVal.replace(forbidden, '')

    print("2)금지된 단어", newStr)

    # 중복된 단어 - 등장 횟수를 카운팅할 딕셔너리
    dic_count = {}

    for i in newStr.split():
        try:  # 이미 등장한 값의 경우
            dic_count[i.lower()] += 1
        except:  # 처음 등장한 값의 경우
            dic_count[i.lower()] = 1

    print("dic_count = ", dic_count)

    # 가장 많이 중복된 값
    print("result = ", max(dic_count, key=dic_count.get))


if __name__ == '__main__':
    most_common_word(paragraph, banned)
