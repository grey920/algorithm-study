input = [1, 4, 3, 2]

# 내림차순 정렬
input.sort(reverse=True);
# print( input )

# 홀수번째 인덱스 값들의 합
sum = 0
for i in range(1, len(input), 2):
    sum += input[i]
print(sum)
