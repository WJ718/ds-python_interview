"""
입력: 2, [[1,0]]
출력: true

[접근방식]
순환구조인지 판별하기
"""
from typing import List
import collections

def courseSchedule(num: int, course: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    for x, y in course:
        graph[x].append(y) # ex) 'x': ['y1', 'y2']

    traced = set() # 현재 DFS 재귀 경로
    visited = set() # 완료 처리된 정점

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 검증 끝난 노드이면 True
        if i in visited:
            return True
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
            
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)
        return True
    
    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
        
    return True