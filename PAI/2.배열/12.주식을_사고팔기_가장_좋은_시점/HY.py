from functools import reduce
from typing import List

# 12. 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
#
# 예제 1
# 입력
nums = [7, 1, 5, 3, 6, 4]


# 조건

# 출력
# 5
# 1일 때 사서 6일 때 팔면 5의 이익을 얻는다.

# buy 값을 저장 -> value 값이 buy 값보다 작으면 덮어쓴다.
# ex) 7 -> 1 작기 때문에 buy 에 저장
# sell 값을 저장 -> buy 값보다 크고 기존에 있는 sell 보다 크면 덮어쓴다.
# ex) 5 저장 -> 5 > 3 저장안함 -> 5 < 6 sell에 저장

def solution():
    print("start")

    buy = 0
    sell = 0

    for i, value in enumerate(nums):
        if buy > value or i == 0:
            buy = value
            continue
        if buy < value > sell:
            sell = value

    result = sell - buy

    print(buy, "일 때 사서", sell, "일 때 팔면", result, "의 이익을 얻는다.")
    print("end (result) : ", result)
    print("전체 시간 복잡도는 O(n)")


if __name__ == '__main__':
    solution()
