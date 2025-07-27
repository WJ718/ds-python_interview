"""
가까운 두 수끼리 위치 바꾸기
예시) 1->2->3->4
출력) 2->1->4->3

사용방법: 반복문 사용

1 > 2 > 3 > 4 > 5 > 6
2를 prev라고 칭하고. 3(a), 4(b) 번째 스왑

b = a.next
a.next = b.next
b.next = a // 스왑은 되었으나 prev에서 위치가 바뀐 b로 안이어짐

prev.next = b // 따라서 연결 필요


"""

class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        node = self
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

def swapLinkedList(head: LinkedList) -> LinkedList:
    root = prev = LinkedList(None)
    prev.next = head

    while head and head.next:
        # b = a.next
        b = head.next
        # a -> c
        head.next = b.next
        # b.next = a  >>>>  a <--> b swap 
        b.next = head

        # prev -> b >>> prev -> b -> a -> c
        prev.next = b

        # head = c
        head = head.next
        # prev = a
        prev = prev.next.next

    return root.next

case = testcase([1,2,3,4,5,6])
result = swapLinkedList(case)
print(result)