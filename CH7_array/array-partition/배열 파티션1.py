"""
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수 구하기

예시 데이터 [1,4,3,2]

답: min(1,2) + min (3,4) = 4

1. sort 후 오름차순으로 min 페어 구하기
2. 짝수번째 합 구하기

"""
from typing import List

testcase = [1,4,3,2]

def arrPartition(s: List[int]) -> int:
    s.sort() # 오름차순 정리
    l = len(s)
    result = 0

    for i in range(l):
        if i % 2 == 0:
            result += s[i]

    return result

print(arrPartition(testcase))
