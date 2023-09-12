import re


# 13. 팰린드롬 연결 리스트
# 연결 리스트가 팰린드롬 구조인지 판별하라.
#
# 예제 1
# 입력
# "1->2"

# 출력
# false

# 예제 2
# 입력
# "1->2->2->1"

# 출력
# true

def solution(value: str):
    print("start")

    # 정규 표현식을 사용하여 문자와 숫자만 추출
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', value)

    print('cleaned_text[::-1] = ', cleaned_text[::-1])
    return cleaned_text == cleaned_text[::-1]


if __name__ == '__main__':
    text1 = "1->2"
    text2 = "1->2->2->1"
    solution_1 = solution(text1)
    solution_2 = solution(text2)

    print('end : ', text1, '-> solution_1 = ', solution_1)
    print('end : ', text2, '-> solution_2 = ', solution_2)
    print("전체 시간 복잡도는 O(n)")
