def trap( height):
    # 막대를 담을 스택 생성
    stack = []
    # 리턴할 값
    volume = 0

    #  주어진 input인 height의 길이만큼 반복
    for i in range(len(height)):
        # 변곡점을 만나는 경우 (이전 높이보다 현재가 높을 때)
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 첫번재 요소를 꺼낸다. (이전 높이)
            top = stack.pop()

            # 스택이 비어있으면 (전전값이 존재하지 않으면 물이 채워질 곳이 없다.)
            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            # 현재 막대의 위치 - 전전 막대의 위치 - 1 (가로길이)
            distance = i - stack[-1] - 1
            # 더 낮은 막대를 기준으로 물 높이 맞춤. (세로길이. while 반북을 돌면서 height[top]을 바닥으로 잡고 물을 채워나감.)
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
