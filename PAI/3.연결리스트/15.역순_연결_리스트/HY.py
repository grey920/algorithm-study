import re
from collections import deque


# 15. 역순 연결 리스트
# 연결 리스트를 뒤집어라.
#
# 예제 1
# 입력
# 1->2->3->4->5->NULL

# 출력
# 5->4->3->2->1->NULL

def solution(value: str):
    print("start", value)

    string_value = value.split("->")
    string_value.reverse()
    print("string_value = ", string_value)
    my_list = deque(string_value)

    # 0번째 인덱스에 있는 값을 마지막 인덱스로 옮김
    my_list.rotate(-1)
    print("my_list =", my_list)

    # 정렬된 숫자 리스트를 문자열로 변환
    result = "->".join([str(val) for val in my_list])

    print('result', result)
    print("전체 시간 복잡도는  O(n + m)")

if __name__ == '__main__':
    input_val = "1->2->3->4->5->NULL"

    solution(input_val)
