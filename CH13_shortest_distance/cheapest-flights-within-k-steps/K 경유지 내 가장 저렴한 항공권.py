"""
리디코드) K경유지 내 가장 저렴한 항공권 문제
n = 노드 개수, edges = [[시작, 끝, 가중치]]
src = 시작 노드 , dst = 도달 노드, K = x개의 경유지

[접근방법]
dijstra를 확장시킨다. 
1. 기존의 매개변수인 start, graph, n 이외에도 end와 K를 추가함
2. dist는 1차원 배열이 아닌, 2차원 배열로 생성 - 행: n개, 열: K+2개의 간선 (정점 u부터 간선 s개를 이용할 때의 최단거리)
3. 최소힙이 있을 때, cur, u이외에 stops라는 변수도 함께 저장하고 꺼냄. stops = 경유지의 개수임
4. 최단거리 가지치기는 동일하며, u == end일때, 답을 리턴, stops와 K가 같으면 경유지를 초과했으므로 탐색중지
5. min(dist[end])를 통해 최단값을 리턴
"""
import collections
import heapq

n = 3
edges = [[0,1,100], [1,2,100], [0,2,500]]
src = 0
dst = 2
K = 0
graph = collections.defaultdict(list)

def dijstra(start, end, graph, n, K):
    INF = float('inf')
    # dist[u][s] : 노드 u에 s개의 경유지(간선)를 써서 도착하는 최소 비용
    dist = [[INF] * (K+2) for _ in range(n)]  # 의문 - 왜 K+2만큼인가 --> dist 는 간선 표이기 때문에 최소 0~K+1까지 필요
    dist[start][0] = 0

    pq = [(0, start, 0)] # 현재 비용, 현재 노드, 사용한 경유지 수

    while pq:
        cur , u, stops = heapq.heappop(pq)

        # 최단거리 가지치기
        if cur > dist[u][stops]:
            continue
     
        # 목적지 도달 시 반환 가능
        if u == end:
            return cur
        
        # 경유지 수가 K개 넘길 시 탐색 X
        if stops > K:
            continue
        
        for v, w in graph[u]:
            nd = cur + w
            ns = stops + 1   # 항공편 증가
            if nd < dist[v][ns]:
                dist[v][ns] = nd
                heapq.heappush(pq, (nd,v,ns))

    ans = min(dist[end])
    return -1 if ans == float('inf') else ans
        
# 그래프 생성
for a,b,w in edges:
    graph[a].append((b,w))

# 다익스트라 호출
answer = dijstra(src, dst, graph, n, K)
print(answer)




