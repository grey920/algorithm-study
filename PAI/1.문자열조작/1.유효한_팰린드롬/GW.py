import re

input = "A man, a plan, a canal: Panama"

# 1. 모두 소문자로 바꾼다
new_input = input.lower()
# print( new_input )

# 2. 영문자와 숫자만 남긴다
new_input = re.sub('[^a-zA-Z0-9]', '',  new_input );
# print( new_input )
# print( len(new_input) // 2 )
# print( len(new_input) // 2 + 1 )

# 3. slice
half = new_input[: len(new_input) // 2 ]
half2 = new_input[ len(new_input) // 2 + 1 :]
# print( half )
# print( half2[::-1] )

# 4. 반쪽이 맞나 검증
if half == half2[::-1]:
    print( 'true' )
else:
    print('false')