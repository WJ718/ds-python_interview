"""
제공된 리스트 내에서 목표 합이 되는 조합을 새로운 리스트에 담아 출력

입력: candidates = [2,3,6,7], target = 7
출력: 
[
    [7],
    [2,2,3]
]
"""
from typing import List

def findComb(lst: List[int], t: int) -> List[List[int]]:
    result = []

    # csum : 남은 합, index : 해당 단계의 시작 인덱스, path : 지금까지 선택한 숫자들의 목록
    def dfs(csum , index, path):
        if csum < 0: # 목표 초과 시 가지치기
            return
        if csum == 0: # target에 해당되는 조합은  result에 추가
            result.append(path)
            return
        
        # 현재  인덱스부터 끝까지 후보를 보며 
        for i in range(index, len(lst)):
            dfs(csum - lst[i], i , path + [lst[i]])

    
    dfs(t, 0 , [])
    return result

    