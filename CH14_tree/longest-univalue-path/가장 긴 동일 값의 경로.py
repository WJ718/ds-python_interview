"""
동일한 노드간 이동할 수 있는 가장 긴 거리 (간선) 을 출력하라
    5
   / \
  4   5
 / \   \
1   1   5 

5->5->5 로, 출력은 2

[접근방법]
<1- BFS>
1. 루트를 하나씩 꺼내서, 왼쪽 자식과 오른쪽 자식을 센다.
2. 루트와 자식이 숫자가 같다면, 길이를 증가시킨다. 
3. 루트와 자식 간 숫자가 다르다면, 길이를 증가시키지 않아야함

<2-DFS>
1. 현재 노드에서 시작해서 같은 값으로 이어질 수 있는 "최대 길이(간선 수)"를 반환
2. 전역 변수(ans)를 두어, 왼쪽 경로 길이 + 오른쪽 경로 길이의 합으로 갱신.

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

ans = [0]


def dfs(node):    
    if not node:
        return 0
    
    # 해당 단계 노드의 왼쪽 가지 최댓값
    left = dfs(node.left)
    right = dfs(node.right)

    left_path = right_path = 0

    if node.left and node.left.val == node.val:
        left_path = left + 1

    if node.right and node.right.val == node.val:
        right_path = right + 1

    ans[0] = max(ans[0], left_path + right_path)

    return max(left_path, right_path)

values = [5,4,5,1,1,5]
root = buildTree(values)
answer = dfs(root)
print(answer)