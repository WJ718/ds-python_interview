"""
1->2->3->4->5->NULL

1->3->5->2->4->NULL

"홀수번째 노드를 우선 오름차순으로 연결시키고, 이후에 짝수번째 노드를 오름차순으로 연결시킨다."

공간복잡도 O(1) --> 별다른 추가 리스트 없이, 포인터로 해결
시간복잡도 O(n) --> 한 번의 반복으로, odd 와 even을 동시처리

"""

class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        node = self
        result = []
        
        while node:
            result.append(str(node.val))
            node = node.next
        
        return '->'.join(result)

def testcase(vals):
    head = LinkedList(vals[0])
    node = head

    for val in vals[1:]:
        node.next = LinkedList(val)
        node = node.next
    
    return head

def oddevenLinkedList(head: LinkedList) -> LinkedList:
    if head is None:
        return None

    # 홀수 시작
    odd = head
    # 짝수 시작
    even = head.next
    # 짝수의 헤드
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head

tc = testcase([1,2,3,4,5])
result = oddevenLinkedList(tc)
print(result)