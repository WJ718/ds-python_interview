"""
11110
11010
11000
00000

1: 육지
0: 물

상하좌우로만 연결된 1의 개수를 구하기 (대각선은 X)

[접근방식]
DFS사용
2중 for문으로 전체 격자를 탐색 -- grid[i][j] == '1'인 지점이 있으면:
    DFS 호출    
    섬의 개수 += 1
    
DFS 내부에서는:
    현재 위치를 '0'으로 바꾼다 (방문 처리)
    상하좌우 4방향으로 이동하며 재귀적으로 DFS 호출
"""

# 매개변수 -- 입력으로 들어온 2D 그리드 맵
def findIslands(grid):
    if not grid:
        return 0

    n, m = len(grid), len(grid[0]) # n : 열, m : 행

    def dfs(x, y):
        # 범위 밖이면 종료
        if x<0 or x >= n or y < 0 or y >= m or grid[x][y] == '0':
            return

        # 범위 안일 시 방문 표시
        grid[x][y] = '0' 

        # 상하좌우 탐색
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

    count = 0
    for i in range(n):
        for j in range(m):
            # 현재 땅이 섬이라면
            if grid[i][j] == '1':
                # 재귀적 탐색
                dfs(i,j)
                # 탐색이 끝나면 카운트 증가
                count += 1

    return count