"""
역순으로 저장된 연결리스트의 숫자를 더하기

input : (2->4->3) + (5->6->4)
output : 7 -> 0 -> 8

# reverse()
3->4->2
4->6->5

# list -> integer
8 0 7

# make LinkedList
7->0->8

1. 연결리스트를 역순으로 바꾸고 문자열로 변형
2. 형변환을 통한 덧셈
3. 연결리스트로 출력

"""
from typing import List

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
        
        return ' -> '.join(result)

def createLinkedList(values):
    head = LinkedList(values[0])
    node = head

    for val in values[1:]:
        node.next = LinkedList(val)
        node = node.next

    return head

def reversedLinkedList(head: LinkedList) -> LinkedList:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev

def toInt(node: LinkedList) -> int:
    result = 0
    multiplier = 1
    while node:
        result += node.val * multiplier
        multiplier *= 10
        node = node.next

    return result

def toList(num : int) -> LinkedList:
    head = LinkedList(num % 10)
    num //= 10
    current = head

    while num:
        current.next = LinkedList(num%10)
        current = current.next
        num //= 10
    
    return head


# 테스트케이스 생성
case1 = createLinkedList([2,4,3])
case2 = createLinkedList([5,6,4])

# 역순변환
case1 = reversedLinkedList(case1)
case2 = reversedLinkedList(case2)

# 리스트를 정수로 바꾸기
num1 = toInt(case1)
num2 = toInt(case2)

total = num1+num2

result = toList(total)
print(result)











