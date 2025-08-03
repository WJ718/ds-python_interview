"""
input
[73,74,75,71,69,72,76,73]
output
[1,1,4,2,1,1,0,0]

스택을 쌓다가, 이전보다 상승하는 지점(current)이 있다면 반복  [참고로, 스택에는 온도가 아닌 인덱스를 저장]
    스택에서 가장 최근에 쌓은 지점을 last로 칭하고, pop한다.
    answer[last] = i - last
"""

testcase = [73,74,75,71,69,72,76,73]
l = len(testcase)
stack = []
answer = [0] * l

for i in range(l):
    # 스택이 비어있지 않고, 최근에 저장한 인덱스가 기존보다 크다면 반복한다.
    while stack and testcase[i] > testcase[stack[-1]]:
        # pop해가면서 최종 답안을 구함
        last = stack.pop()
        answer[last] = i - last
    
    stack.append(i)

print(answer)
