from typing import List

def arrayPairSum(nums: List[int]) -> int:
    # sumValue = 0
    # nums.sort()
    #
    # for i, n in enumerate(nums):
    #     if i % 2 == 0:
    #         sumValue += n
    #
    # return sumValue  # 계산된 합을 반환합니다.

    return sum(sorted(nums)[::2])

print(arrayPairSum([1, 4, 3, 2]))



