from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left= left
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

def merge(tree1 : TreeNode, tree2:TreeNode):
    if not tree1 and not tree2:
        return None
    
    if not tree1:
        return tree2
    
    if not tree2:
        return tree1
    
    root = TreeNode(tree1.val + tree2.val)
    root.left = merge(tree1.left , tree2.left)
    root.right = merge(tree1.right , tree2.right)

    return root
    
def printTree(root: TreeNode):
    if not root:
        print([])
        return
    
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

    while result and result[-1] is None:
        result.pop()
        
    print(result)

values1 = [1,3,2,5]
values2 = [2,1,3,None,4,None,7]

tree1 = buildTree(values1)
tree2 = buildTree(values2)

ans = merge(tree1, tree2)
printTree(ans)








