# 문제집 풀이
input = [1, 2, 3, 4]
out = []
# 곱셈 기본값 1
p = 1
# 투 포인터처럼 자신을 기준으로 왼쪽 곱셈 x 오른쪽 곱셈 을 한다
# 왼쪽부터 곱셈
for i in range(0, len(input)):
    # 1부터 곱셈을 out 배열에 차례로 넣어준다
    out.append(p)
    p *= input[i]
# print(out)

# 왼쪽부터 곱해진 out 배열에 오른쪽 값을 차례로 곱한다
p = 1
for i in range(len(input)-1, -1, -1 ): # 가장 마지막 인덱스부터 0번 인덱스까지 역순으로 반복
    out[i] *= p
    p *= input[i]
print(out)


# O(n^2) 였던 시도
# from functools import reduce
#
# input = [1, 2, 3, 4]
# output = []
# dict = {}
#
#
# # n
# def get_multiple_num( arr ):
#     return reduce(lambda x, y: x * y, arr)
#
# # n^2
# for i in range(len(input)):
#     # 딕셔너리의 값에 나를 제외한 값들을 담는다
#     copy_input = input.copy() # n
#     copy_input.remove(input[i])
#     dict[input[i]] = copy_input
# print(dict)

# output 배열에 곱해서 넣어준다
# for key in dict:
#     output.append( get_multiple_num(dict[key]) )
# print(output)