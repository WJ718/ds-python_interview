"""
[입력]
     4
    / \
   2   7
  / \  / \
 1   3 6  9

[출력]
      4
    /   \
   7     2
  / \   / \
 9   6 3   1

right를 left로 보내기

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

def reversalTree(root: TreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)

    return root

def printTree(root: TreeNode):
    if not root:
        print([])
        return
    
    # 출력용 리스트
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        else:
            result.append(None)

    # 출력에 None은 제거
    while result and result[-1] is None:
        result.pop()
    
    print(result)



values = [4,2,7,1,3,6,9]
root = buildTree(values)
ans = reversalTree(root)
printTree(ans)





    

