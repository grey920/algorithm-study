# 로그를 재정렬하라. 기준은 다음과 같다.
# 1. 로그의 가장 앞 부분은 식별자다.
# 식별자 -> dig1, let1, dig2, let2, let3
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# "let1 art can" "let2 own kit dig" "let3 art zero" "dig1 8 1 5 1" "dig2 3 6"
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 'art can' 'art zero' = 'art' 동일? => "let1 art can" "let3 art zero" "let2 own kit dig"
# 4. 숫자 로그는 입력 순서대로 한다. -> "dig1 8 1 5 1", "dig2 3 6"
from typing import List


def reorder_log_files(inputVal: List[str]):
    print("Reorder Log Files = ", inputVal)
    print("Reorder Log Files type = ", type(inputVal))

    # 문자와 숫자 구분
    strList, numList = [], []

    # 문자만 있는 로그
    for i in inputVal:
        print("문자 전체 = ", i, "로그 첫번째 = ", i[5], "숫자판별 = ", i[5].isdigit())

        if i[5].isdigit():
            numList.append(i)
        else:
            strList.append(i)

    # 문자 순서 변경( 동일한 문자가 있는 경우 )
    print("숫자 = ", numList)
    print("문자 = ", strList)
    strList.sort(key=lambda x: (x.split()[1], x.split()[2]))
    print("문자 정렬 = ", strList)

    result = strList + numList
    print("결과=", result)


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
logs2 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let4 art can", "let3 art zero"]
output = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
output2 = ['let1 art can', 'let4 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
if __name__ == '__main__':
    reorder_log_files(logs2)
