"""
[
    1->4->5,
    1->3->4,
    2->6
]

k개의 정렬된 리스트를 하나로 병합하는 문제

[접근방법]
우선순위 큐 사용 (heapq)

"""

import heapq # 최소 힙 모듈
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLists(self, lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = [] # (값, 리스트번호, 노드) 

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            # heapq는 자동으로 노드값이 작은 순서로 정렬
            heapq.heappush(heap, (lists[i].val, i, lists[i]))   
            """
                heap = [
                    (1, 0, ListNode(1)),  # 1->4->5
                    (1, 1, ListNode(1)),  # 1->3->4
                    (2, 2, ListNode(2))   # 2->6
                ]
            """

    
    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        # 가장 작은 노드 꺼내와 result에 추가
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        # 포인터를 한 칸 옆으로
        result = result.next
        # 만약 방금 넣은 노드가 다음 노드를 가진다면 해당 노드를 heapq에 넣어 다시 정렬
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

        
    return root.next

