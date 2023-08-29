
nums = [2, 7, 11, 15]
target = 9

dict = {}
for i in range( len( nums ) ):
    # nums를 딕셔너리에 저장. key는 인덱스, value는 값
    dict[nums[i]] = i
    
    # 딕셔너리 안에 타겟을 만들 수 있는 값이 있는지 체크
    if ( target - nums[i] ) in dict:
        print(  list( ( dict[target - nums[i]], dict[nums[i]] ) ) )
        break

