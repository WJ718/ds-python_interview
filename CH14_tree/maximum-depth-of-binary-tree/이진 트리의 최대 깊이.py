"""
이진 트리의 최대 깊이를 구하라
input이 [3, 9, 20, null, null, 15, 7]로 주어졌을 때,

  3
 / \
9   20
    / \
   15  7

깊이는 3이다.

[접근방식]
BFS -> queue

"""
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# root : 인풋으로 받을 리스트
def maxDepth(root : TreeNode) -> int:
    if not root:
        return 0
    
    depth = 0
    # 데크에 삽입 (루트 노드 하나만 들어있음.)
    queue = deque([root])

    while queue:
        # 데크의 길이만큼 반복
        for _ in range(len(queue)):
            
            node = queue.popleft() 

            # 해당 노드에 left, right 노드가 있는지 점검
            # 있다면, 새롭게 데크에 추가함.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        depth += 1
    
    return depth


def buildTree(values):
    if not values or values[0] is None:
        return None
    
    # 리스트의 첫 번째 수를 루트로 생성
    root = TreeNode(values[0])
    # 데크에 삽입
    queue = deque([root])
    # 반복을 위한 i 지정
    i = 1

    # 데크가 있으면서 i가 리스트의 길이보다 작을 시
    while queue and i < len(values):
        node = queue.popleft()

        """ 한 사이클에 두 개의 자식을 바로 처리 """

        # left 부터 채우기
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            # 데크에 추가함으로써 다음 자식 대비
            queue.append(node.left)
        
        i += 1 

        # right도 채우기
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

values = [3,9,20,None,None,15,7]
root = buildTree(values)

print(maxDepth(root))