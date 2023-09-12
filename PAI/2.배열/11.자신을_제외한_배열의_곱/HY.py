from functools import reduce
from typing import List

# 11. 자신을 제외한 배열의 곱
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
#
# 예제 1
# 입력
nums = [1, 2, 3, 4]


# 조건
# 나눗셈을 하지 않고 O(n)에 풀이하라

# 출력
# [24, 12, 8, 6]

def solution():
    print("start")

    result: list[int] = []

    # 시간복잡도 => O(n^2)

    # for i in range(len(nums)):
    #     # 현재 인덱스를 제외한 새로운 리스트 생성
    #     current_list = nums[:i] + nums[i + 1:]
    #     other_lists.append(current_list)
    #
    # print(other_lists)

    # 시간복잡도 => O(n^2)

    # for i in range(len(nums)):
    #     other_lists = list(nums)
    #     other_lists.pop(i)
    #
    #     print('other_lists = ', other_lists)
    #
    #     result.append(reduce(lambda x, y: x * y, other_lists))

    # 빈 딕셔너리
    result_dict = {}

    # 리스트를 순회하면서 중복된 값이 나타날 때마다 카운트를 증가시켜 딕셔너리에 추가
    for i, value in enumerate(nums):
        key = i  # key를 숫자에서 문자열로 변환
        other_lists = list(nums)
        other_lists.pop(i)

        print('=======', key, other_lists)

        result_dict[key] = other_lists

    for i in range(len(nums)):
        i_ = result_dict[i]
        result.append(reduce(lambda x, y: x * y, i_))

    print("end (result_dict) : ", result_dict)
    print("end (result) : ", result)
    print("전체 시간 복잡도는 O(n^2)")


def product_except_self(nums):
    n = len(nums)

    # 왼쪽에서의 누적 곱 배열
    left_product = [1] * n
    left_product[0] = 1

    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]

    # 오른쪽에서의 누적 곱 및 결과 배열
    right_product = 1
    output = [0] * n

    for i in range(n - 1, -1, -1):
        output[i] = left_product[i] * right_product
        right_product *= nums[i]

    return output


if __name__ == '__main__':
    solution()
    # 해설
    result = product_except_self(nums)
    print('해설 = ', result)
