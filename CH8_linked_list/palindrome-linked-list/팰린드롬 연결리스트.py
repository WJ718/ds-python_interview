"""
입력: 1->2
출력: false

입력: 1->2->2->1
출력: true

주의 할 점 : 입력 형태가 연결 리스트라고 가정하고, 문제를 풀어야 한다.

데크 사용: 입력받은 순서대로 데크에 저장하고, popleft(), pop()을 통해 비교

[typing 라이브러리]
typing.Tuple = 여러개의 정해진 인자를 사용할 때 ex) example[int, float]
typing.Union = 인자가 다양한 종류를 받을 수 있을 때 ex) example[int, str] # 정수 또는 문자열을 인자로 받을 수 있음
typing.Optional = 인자가 None일 때 사용



"""
from typing import Optional, Deque
import collections

# 클래스 생성 - 연결 리스트 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 팰린드롬 판별 메서드
def isPalindrome(head: Optional[ListNode]) -> bool:
    # 변수 q의 타입: Deque / 값: collections.deque()
    q: Deque[int] = collections.deque() 

    # 요소를 데크에 추가
    while head:
        q.append(head.val)
        head = head.next

    # 가장자리부터 비교
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
        
    return True

# testcase 생성
def create_testcase(values):
    head = ListNode(values[0])
    node = head

    for val in values[1:]:
        node.next = ListNode(val)
        node = node.next

    return head

# 테스트
if __name__  == "__main__":
    testcase = input("").split('->')
    values = list(map(int, testcase))
    head = create_testcase(values)

    print(isPalindrome(head))


