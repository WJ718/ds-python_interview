"""
직렬화 : 트리를 리스트 형태로 만드는 것
역직렬화 : 리스트를 트리 형태로 만드는 것


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

values = [1,2,3,None,None,4,5]
root = buildTree(values)

# 직렬화 코드 -> BFS
def serializeTree(root: TreeNode):
    result = [] # 직렬화 결과를 내놓을 리스트

    # 트리를 만들 떄 썻던 방법으로 요소 하나하나를 리스트에 저장
    queue = deque([root])

    while queue:
        # 루트노드부터 시작
        node = queue.popleft() 
       
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    
    return result
 
# 역직렬화 코드 
def deserializeTree(data):
    if not data or data[0] is None:
        return None
    
    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        node = queue.popleft()

        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i+=1

        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i+=1
    
    return root

    

