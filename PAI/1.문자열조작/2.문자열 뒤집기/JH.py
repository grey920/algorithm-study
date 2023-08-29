from typing import List


def reverse_list(target_list: List[str]) -> None:
    target_list.reverse()

    return None


list1: List[str] = ["h", "e", "l", "l", "o"]
list2: List[str] = ["H", "a", "n", "n", "a", "h"]

reverse_list(list1)
reverse_list(list2)

print(list1)
print(list2)
