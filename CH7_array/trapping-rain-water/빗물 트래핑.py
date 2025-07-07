from typing import List

testcase = [0,1,0,2,1,0,1,3,2,1,2,1]

def traping(h: List[int]) -> int:
    stack = []
    v = 0 # 쌓인 물의 양
    
    for i in range(len(h)):
        # 현재 높이가 스택의 가장 위보다 높을 경우 --> 구덩이 발견
        while stack and h[i] > h[stack[-1]]:

            # top = 바닥의 높이가 있는 인덱스
            top = stack.pop()

            if not len(stack):
                break
            
            # 너비 (두 벽 사이의 칸 수)
            width = i - stack[-1] - 1
            # 높이 (더 낮은 벽의 높이 - 바닥의 높이)
            height = min(h[i], h[stack[-1]]) - h[top]

            v += width * height

        # 스택에는 인덱스를 push함
        stack.append(i)
    
    return v

print(traping(testcase))


