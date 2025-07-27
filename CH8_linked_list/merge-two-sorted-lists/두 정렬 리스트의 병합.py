"""
정렬된 두 연결 리스트를 합쳐라

1->2->4, 1->3->4
: 1->1->2->3->4->4

재귀처리
리스트1이 없거나, 리스트1->val > 리스트2->val 일 경우, 두 리스트의 값을 뒤바꿈
"""

# 연결리스트 클래스 생성
class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 병합 메서드
def mergeList(l1: LinkedList, l2:LinkedList) -> LinkedList:
    # l1을 다 돌았거나 l2보다 클 때
    if not l1 or (l2 and l1.val > l2.val):
        # 더 작은 값을 가진 노드를 l1으로 만들기 위해 위치 교환
        l1,l2 = l2, l1
    # l1이 남아있다면
    if l1:
        # 재귀 (l1.next에 l1.next와 l2의 병합 결과를 연결)
        l1.next = mergeList(l1.next, l2)

    return l1

# 테스트케이스 생성 메서드
def testcase(values):
    # 헤드 설정
    head = LinkedList(values[0])
    node = head

    for val in values[1:]:
        node.next = LinkedList(val)
        node = node.next
    return head

# 메인 메서드 실행
l1 = testcase([1,2,4])
l2 = testcase([1,3,4])
result = mergeList(l1,l2)

output = []
while result:
    output.append(str(result.val))
    result = result.next

print('->'.join(output))
    
