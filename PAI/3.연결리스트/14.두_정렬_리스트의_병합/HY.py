import re


# 14. 두 정렬 리스트의 병합
# 정렬되어 있는 두 연결 리스트를 합쳐라.
#
# 예제 1
# 입력
# 1->2->4, 1->3->4

# 출력
# 1->1->2->3->4->4

def solution(value1: str, value2: str):
    print("start", value1, value2)

    # string_value = "->".join([value1, value2])
    # print("string_value", string_value)

    # 정규 표현식을 사용하여 문자와 숫자만 추출
    # cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', string_value)
    # print("cleaned_text", cleaned_text)

    string_value = value1.split("->")
    numbers_str = value2.split("->")

    string_value.extend(numbers_str)

    number_list = [int(char) for char in string_value]
    print("number_list", number_list)

    # 오름차순 정렬
    sorted_numbers = sorted(number_list)
    print("sorted_numbers", sorted_numbers)

    # 정렬된 숫자 리스트를 문자열로 변환
    result = "->".join([str(num) for num in sorted_numbers])

    print('result', result)
    print("전체 시간 복잡도는  O(n1 + n2 * log(n1 + n2))")


if __name__ == '__main__':
    text1 = "1->2->4"
    text2 = "1->3->4"

    solution(text1, text2)
