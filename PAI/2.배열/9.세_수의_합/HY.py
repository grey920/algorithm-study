from typing import List

# 09. 세 수의 합
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
#
# 예제 1
# 입력
nums = [-1, 0, 1, 2, -1, -4]


# 정렬
# [-4, -1, -1, 0, 1, 2]

# 0이 되려면 ?
# -4 => -1 = +5

# 출력
# [
#    [-1, 0, 1],
#    [-1, -1, 2]
# ]

def solution():
    print("start")

    # 리스트의 길이를 구합니다.
    n = len(nums)

    # 결과를 담을 리스트
    result = []

    # 빈 딕셔너리를 생성하여 해당값이 있는지 확인할 것입니다.
    result_dict = {}

    # 주어진 리스트의 모든 숫자에 대해 반복합니다.
    for value in nums:
        key = str(value)
        # 딕셔너리에 해당 숫자의 등장 횟수를 기록합니다.
        if key in result_dict:
            result_dict[key] += 1
        else:
            result_dict[key] = 1

    # 리스트에서 세 수의 합이 0이 되는 조합을 찾기 위해 이중 반복문을 사용합니다.
    for i in range(n):
        for j in range(i + 1, n):
            sumNum = 0
            if nums[i] > nums[j]:
                # 첫번째 값이 더 큰 경우 두 숫자의 합을 음수로 변경
                sumNum = -sum([nums[i], nums[j]])
            else:
                sumNum = sum([nums[j], nums[i]])

            # 합이 딕셔너리에 있는지 확인합니다.
            if str(sumNum) in result_dict:

                # 중복을 처리하기 위한 조건
                if result_dict[str(sumNum)] == 1 and nums[i] == sumNum:
                    continue

                # 합이 0이 되는 경우, 결과 리스트에 세 숫자를 추가합니다.
                if sumNum + nums[i] + nums[j] == 0:
                    sumList = [nums[i], nums[j], sumNum]
                    result.append(sumList)

    # 중복된 결과 제거
    unique_result = []
    for triplet in result:
        triplet.sort()
        if triplet not in unique_result:
            unique_result.append(triplet)

    print("end (result) : ", unique_result)


if __name__ == '__main__':
    solution()
