import re


def validate_palindrome(text: str) -> bool:
    text = re.sub('[^a-z0-9]', "", text.lower())

    reverse_lower_text: str = text[::-1]

    print(text)
    print(reverse_lower_text)


    for i in range(len(text)):

        if reverse_lower_text[i] != text[i].lower():
            return False

    return True


print(validate_palindrome("A man, a plan, a canal : Panama"))

print(validate_palindrome("race a car"))

