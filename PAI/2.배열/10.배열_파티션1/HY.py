from typing import List

# 10. 배열 파티션1
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
#
# 예제 1
# 입력
nums = [1,4,3,2,0]


# 출력
# 4
# n은 2가 되며, 최대 합은 4이다.
# min(1,2) + min(3,4) = 4이다.

# 1) 정렬 = 작은 수 -> 큰 수로 정렬을 해야 min(작은수, 큰수) 더 큰 작은 수를 얻을 수 있다
# 2) 홀수 인 경우 정렬 후 첫번째 값은 버림

def solution():
    print("start")

    # 결과를 담을 리스트
    result: list[int] = []

    # 정렬
    nums.sort()

    if len(nums) % 2 != 0:
        print('홀수! 제일 작은수 제거', nums[0])
        nums.pop(0)

    # range(start, stop, step)함수를 사용
    # start: 시작값을 나타냅니다. 이 값부터 반복이 시작
    # stop: 반복을 종료할 값입니다. 이 값보다 작은 경우 반복이 계속
    # step: 각 반복 사이의 간격, 이 값은 몇 개씩 증가하거나 감소하는지를 결정
    for i in range(0, len(nums), 2):

        # 슬라이싱을 사용하여 리스트 또는 다른 순차적인 자료형에서 일부 요소를 가져온다.
        # i: 이것은 현재의 반복 인덱스 또는 위치
        # i + 2: 여기에서는 현재 인덱스 i에 2를 더한 값( 현재값 부터 다음 요소 )
        print('페어 값', nums[i])
        pair = nums[i:i + 2]

        # min
        minValue = min(pair)

        result.append(minValue)

    print("end (result) : ", sum(result))
    print("전체 시간 복잡도는 O(n log n)")


if __name__ == '__main__':
    solution()
