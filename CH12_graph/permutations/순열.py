"""
입력: [1,2,3] (리스트형태)
출력: 순서를 포함한 모든 조합 --> itertools.permutations 사용하기
"""
from typing import List
import itertools

def permutations(lst: List):
    l = len(lst)
    # 출력 형태를 위해 각 요소를 리스트로 감싸기
    return  [list(p) for p in itertools.permutations(lst, l)]

print(permutations([1,2,3]))