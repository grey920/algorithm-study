nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
# print( "sorted nums :::::: ", nums )

result = []
# 포인터
left = 0
right = len( nums ) - 1

for i in range( len(nums) - 2 ):
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i-1]:
        continue

    left = i + 1
    right = len( nums ) - 1

    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            result.append( [nums[i], nums[left], nums[right]] )

            # 중복된 값 건너뛰기
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1

            left += 1
            right -= 1
print( result )
