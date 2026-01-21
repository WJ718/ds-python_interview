"""
이진트리에서 두 노드간 가장 긴 길이를 출력할 것
       1
     /   \
    2     3
   / \
  4   5

4-2-1-3 으로, 4 출력
"""

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i+=1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i+=1
    
    return root

def findRoute(root: TreeNode) -> int:
    ans = [0] # list 사용 --> 함수 안에서 외부 변수로 갱신가능

    def dfs(node):
        if not node:
            return 0
        
        # 재귀 호출  
        left = dfs(node.left)
        right = dfs(node.right)

        # 재귀가 끝난 후 출력할 최대 길이 계산
        ans[0] = max(ans[0], left + right + 1)

        # left와 right 각각 dfs
        return max(left,right) + 1
    
    dfs(root)
    return ans[0]

values = [1,2,3,4,5]
root = buildTree(values)
print(findRoute(root))
