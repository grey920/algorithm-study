import re
from collections import deque


# 16. 페어의 노드 스왑
# 연결 리스트를 입력받아 페어 단위로 스왑하라.
#
# 예제 1
# 입력
# 1->2->3->4


# 출력
# 2->1->4->3

def solution(value: str):
    print("start", value)

    value_split = value.split("->")
    print("value_split", value_split)

    my_deq = deque(value_split)

    # 짝수 번째에 대해 작업 수행
    for i in range(1, len(value_split), 2):
        # i가 짝수 인덱스인 경우에만 해당 요소에 대해 작업 수행
        print(value_split[i])

        my_deq.remove(value_split[i])

        # 특정 인덱스 앞에 요소 추가
        my_deq.insert(i-1, value_split[i])

    result = "->".join(str(val) for val in my_deq)

    print("result = ", result)
    print("전체 시간 복잡도는  O(n)")


if __name__ == '__main__':
    input_val = "1->2->3->4"

    solution(input_val)
