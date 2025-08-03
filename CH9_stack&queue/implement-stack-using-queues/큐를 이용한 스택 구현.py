"""
큐를 이용해 다음 연산을 지원하는 스택을 구현하기
push() : 요소를 스택에 삽입
pop(): 스택의 첫 번째 요소 삭제
top(): 스택의 첫 번째 요소 가져옴
empty(): 비어있으면 True, 안 비어있으면 False

[접근방법]
데크에 push하는 동시에 정렬을 통해 큐의 맨 앞으로 보낸 후, 꺼낼 때는 popleft() 사용하기
"""

import collections

class Stack:
    def __init__(self):
        self.q = collections.deque()
    
    def push(self, x):
        self.q.append(x)
        # 재정렬
        for _ in range(len(self.q)):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0