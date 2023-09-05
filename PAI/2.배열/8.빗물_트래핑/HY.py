from typing import List

# 07. 두 수의 합
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
# ~ 모양 개수
# 예제 1
# 입력
nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


#                ㅁ
#       ㅁ ~ ~ ~ ㅁ ㅁ ~ ㅁ
# - ㅁ ~ ㅁ ㅁ ~ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ
# 0 1 0 2  1 0 1 3  2 1  2  1
#     1   1  2 1    1 1     1

#     1      1
#          1 1 1      1
# 출력
# 6

# 전체 순환을 시작
# 처음 순회는 1부터 시작합니다.
# 다음 숫자가 현재 숫자보다 작은 경우 count +=  타겟값 - 현재값
# 다음 숫자가 현재 숫자보다 크거나 같은 경우 result_count += count 하고 count 초기화

def rainwater_trapping():
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    # 빈 딕셔너리
    result_dict = {}

    # 리스트를 순회하면서 중복된 값이 나타날 때마다 카운트를 증가시켜 딕셔너리에 추가
    for value in nums:
        key = str(value)  # key를 숫자에서 문자열로 변환
        if key in result_dict:
            result_dict[key] += 1
        else:
            result_dict[key] = 1

    result_count = 0  # 결과를 저장할 변수를 초기화
    current_height = 1  # 처음 순회는 1부터 시작하므로 현재 숫자를 1로 초기화
    current_count = 0  # count를 저장할 변수를 초기화

    for i in range(1, len(nums)):

        if i == 0 and nums[i] == 0:
            continue

        print("start Num = ", nums[i])

        if result_dict[str(nums[i])] == 1:
            continue

        if nums[i] < current_height:
            print(current_height, '-', nums[i], '=', current_height - nums[i])
            current_count += current_height - nums[i]
            print('current_count = ', current_count)
        elif nums[i] >= current_height:
            print('elif = ', nums[i], current_height)
            print('elif current_count = ', current_count)
            result_count += current_count
            print('result_count = ', result_count)
            current_count = 0
            current_height = nums[i]

    print(result_count)



if __name__ == '__main__':
    rainwater_trapping()
