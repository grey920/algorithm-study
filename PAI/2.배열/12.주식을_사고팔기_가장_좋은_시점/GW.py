"""
[9,9,9,9,9,9,9,9] => 이익이 모두 다 0으로 같음
[1,2,3,4,5,6] => 1에서 사서 6에 팔면 이익이 5이다.
[6,5,4,3,2,1] => 계속 내려가므로 0이다.. 슬픈 그래프네..
[1, 2, 3, 4, 3, 2, 1] => 1에 사서 4에 팔면 이익이 3이다.
[3, 2, 1, 2, 3, 4, 5] => 1에 사서 5에 팔면 이익이 4이다.
[2, 1, 3, 2, 5] => 1에 사서 5에 팔면 이익이 4이다.
[1, 3, 2, 5, 4] => 1에 사서 5에 팔면 이익이 4이다.

( 1, 4 )

1. 일단 처음 숫자를 저장
2. 두번째 숫자가 첫번째보다 크면 차액을 담고 continue, 작으면 스택에 값을 바꿔치기 하고 차액은 0으로 한다.
3. 그 다음 숫자가 스택에 담긴 숫자보다 작으면 continue, 크면 차액을 계산해서 스택에 담긴 차액보다 크면 차액을 바꿔담는다. 차액이 스택보다 작으면 continue
4. 모두 끝나면 리턴
"""

list = [7, 1, 5, 3, 6, 4]

def solution( list ):
    # 스택 생성
    stack = []
    # 리스트를 돌면서 진행
    for val in list:
        # 처음에 스택이 비어있으면 넣고 시작
        if not stack:
            stack.append((val, 0))
        else:
            # 스택에 담긴 키와 비교
            if val == stack[-1][0]:
                continue
            if val > stack[-1][0]:
                profit = val - stack[-1][0]
                if profit < stack[-1][1]:
                    continue
                else:
                    top = stack.pop()
                    stack.append((top[0], profit))
                    # print("차액을 바꿔담는다~~ ", stack)
                    continue
            # 스택에 들어있는 키보다 작으면 -> 스택을 바꿔치고 차액을 0으로 초기화
            if val < stack[-1][0]:
                stack.pop()
                stack.append((val,0))
                # print("스택보다 작은 경우! ", stack )
                continue
    return stack[0][1]

print(solution( list ))