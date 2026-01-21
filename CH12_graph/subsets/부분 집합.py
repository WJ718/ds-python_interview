"""
모든 부분 집합 구하기 / 순서는 신경쓰지 않음

nums = [1,2,3]


"""
from typing import List

def findSubsets(lst: List[int]) -> List[List[int]]:
    result = []
        
    def dfs(index, path):
        # 현재 경로를 결과에 추가
        result.append(path)
        # index부터 끝까지 반복
        for i in range(index, len(lst)):
            dfs(i + 1, path + [lst[i]])  # 선택 후 다음 인덱스로 진행
    
    dfs(0, [])
    return result

nums = [1,2,3]
print(findSubsets(nums))