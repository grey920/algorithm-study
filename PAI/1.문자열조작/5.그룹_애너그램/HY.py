import collections
import string
from typing import List

# 05. 그룹 애너그램
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라. -> 문자 같다?
# 예제 1
# 입력
anagram = ["eat", "tea", "tan", "ate", "nat", "bat"]


# 출력
# [
#    ["ate", "eat", "tea"],
#    ["nat", "tan"],
#    ["bat"]
# ]

def group_anagram(inputVal: List[str]):
    print("inputVal = ", inputVal)

    dic = collections.defaultdict(list)
    print("sorted_strs = ", dic)

    for i in inputVal:
        print("기본값 === ", i)
        print("문자 정렬 === ", ''.join(sorted(i)))
        # 정렬된 값을 key 로 설정하여 이미 key가 있다면 value로 저장,
        # 없으면 해당 정렬된 key로 value 추가
        dic[''.join(sorted(i))].append(i)

    print("dict = ", dic)

    # dict 에서 value 만 출력!
    print("result = ", list(dic.values()))


if __name__ == '__main__':
    group_anagram(anagram)
