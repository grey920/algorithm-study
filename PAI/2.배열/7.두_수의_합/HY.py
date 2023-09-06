from typing import List

# 07. 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# 예제 1
# 입력
nums = [2, 7, 11, 15]
target = 9


# 출력
# [0, 1]


def hasDuplicateValue(numList, value):
    return value in numList


def sumToTarget(numList: List[int], targetNum: int):
    print("numList = ", numList)
    print("targetNum = ", targetNum)

    result = []

    for i in range(len(numList)):
        for j in range(len(numList)):
            if j != i:
                print(numList[i])
                print(numList[j])
                if numList[i] + numList[j] == targetNum:
                    # print('firstIndex=', i, 'secondIndex=', j)
                    if not (hasDuplicateValue(result, i) and hasDuplicateValue(result, j)):
                        result.append(i)
                        result.append(j)

    print('result1 = ', result)


def dictTwoSum(nums, target):

    num_dict = {}
    for num in nums:
        num_dict[num] = True

    result = []

    for i, num in enumerate(nums):
        # print('i, num', i, num)
        # 현재값 과 타겟의 값을 뺀다 -> 현재값이 9가 되기위해 필요한 숫자를 뽑는다.
        target_num = target - num
        if num_dict.get(target_num):
            # print('있다', True, i)
            result.append(i)

    return result


def hasValueUsingHashMap(nums, value):
    num_dict = {}
    for num in nums:
        num_dict[num] = True

    return value in num_dict


if __name__ == '__main__':
    sumToTarget(nums, target)
    result = dictTwoSum(nums, target)
    print('result2 = ', result)
