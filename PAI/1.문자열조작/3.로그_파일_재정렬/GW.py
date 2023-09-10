from collections import deque

alpha_queue = deque()
num_queue = deque()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
for i in logs:
    # 1. 문자 숫자 분리
    if i.split(' ')[1].isalpha():
        alpha_queue.append(i)
    else:
        num_queue.append(i)

# 2. 문자 && 문자가 동일하면 식별자 순으로 정렬
for i in alpha_queue:
    print( i.split() )


print( alpha_queue )
print( num_queue )