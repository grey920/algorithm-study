def longest_palindrome(text: str) -> str:
    reverse_text = text[::-1]

    max_string = ""

    for length in range(len(text)):
        for position in range(len(text) - length):

            test = text[position:position + length + 1]

            if test in reverse_text:
                max_string = test
                break

    return max_string


print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
