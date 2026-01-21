"""
[from, to]로 구성된 항공권 목록을 이용하여 JFK에서 출발하는 옇애 일정 구성하기.
일정이 여러개라면, 사전 어휘순으로 방문하기
"""
from typing import List
import collections

def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        
        # 끝에서부터 기록됨
        route.append(a)

    dfs('JFK')

    # 뒤집어주기
    return route[::-1]

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(findItinerary(tickets))