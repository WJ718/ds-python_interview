"""
[input]
1->2->3->4->5->NULL, m = 2, n = 4
[output]
1->4->3->2->5->NULL

기존 연결리스트에서 m ~ n 에 해당하는 부분을 이전에 작성한 reverse() 로직으로 변경하고,
m-1 과 재연결

시간 : O(n-m)
공간 : O(1)

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
    
def createLinkedList(vals):
    head = LinkedList(vals[0])
    node = head

    for val in vals[1:]:
        node.next = LinkedList(val)
        node = node.next
    
    return head

def reverseLinkedList(head: LinkedList, m: int, n: int) -> LinkedList:
    if not head or m == n:
        return head
    
    root = start = LinkedList(None)
    root.next = head

    # select start, end 
    for _ in range(m - 1):
        start = start.next
    
    end = start.next

    for _ in range(n-m):
        temp = end.next           # temp = start 옆으로 붙일 노드
        end.next = temp.next      # end는 움직이지 않고, 다음 노드를 건너뜀
        temp.next = start.next    # 꺼내온 노드를 start.next 앞으로 끼워넣기
        start.next = temp         # 실제로 삽입
                                  # 위의 행동을 반복

    return root.next

testcase = createLinkedList([1,2,3,4,5])
m,n = 2,4

result = reverseLinkedList(testcase, m, n)
print(result)






