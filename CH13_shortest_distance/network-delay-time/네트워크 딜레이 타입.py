"""
모든 노드가 신호값을 받을 수 있는 시간을 계산하라.
입력값[u,v,w] --> u: 출발지, v:도착지, w: 소요시간

1. 모든 노드에 신호를 전달할 수 있는가? - 없다면 -1 반환 --> 그래프가 이어지는가?
2. 1을 통과했다면, 모든 노드가 신호를 받는데 걸리는 가장 늦은 시간 반환  --> 다익스트라

[입력] N: 전체 노드 개수, K: 출발 노드
times = [[2,1,1], [2,3,1], [3,4,1]], N=4, K=2
[출력]
2

[접근방식]
1. collections.defaultdict로 그래프 저장
2. 거리 배열[i]  = k --> i까지의 최단 시간 (처음에는 INF, 시작점 dist[k] = 0)
3. 우선순위 큐(최소 힙) 사용 => heapq에 (현재까지 시간, 노드) 형태로 저장할 것.
"""
import heapq
import collections
import math
from typing import List

def networkDelayTime(times : List[List[int]], N: int, K: int) -> int:
    # 1) 그래프 초기화
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v,w)) # 키: 출발노드  /  값: 도착노드, 시간

    # 2) 거리배열 초기화
    dist = [math.inf] * (N+1)
    dist[K] = 0

    # 3) 우선순위 큐 준비 (최소 힙 : 가자 작은 원소부터 앞에 있음)
    pq = [(0,K)] # (초기 현재까지 걸린시간, 노드)

    # 4) 다익스트라
    while pq: # pq: 지금까지 발견된 후보 경로들을 모아둔 바구니
        cur_time, u = heapq.heappop(pq) # cur_time: 가장 빠른노드
        if cur_time > dist[u]: # 가지치기
            continue

        for v, w, in graph[u]:
            new_time = cur_time + w
            if new_time < dist[v]: # dist[v] = k to v 의 최단시간
                dist[v] = new_time
                heapq.heappush(pq, (new_time, v))

    # 5) 결과 반환 (max)
    max_time = max(dist[1:])
    # 초기에 설정한 inf가 있다면, 그래프가 이어지지 않은 것이므로 -1 반환
    return -1 if math.isinf(max_time) else max_time










    



