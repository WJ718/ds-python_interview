"""
1->2->3->4->5->NULL
5->4->3->2->1->NULL

"""

class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def testcase(values):
    head = LinkedList(values[0])
    node = head

    for val in values[1:]:
        node.next = LinkedList(val)
        node = node.next

    return head

def reverse(head: LinkedList) -> LinkedList:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

test = testcase([1,2,3,4,5])
result = reverse(test)

output = []
while result:
    output.append(str(result.val))
    result = result.next

output.append("NULL")
print("->".join(output))

