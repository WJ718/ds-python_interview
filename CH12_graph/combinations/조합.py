import itertools
from typing import List

def returnCombination(n: int, k:int) -> List[List[int]]:
    return list(itertools.combinations(range(1,n+1), k))

n, k = 4, 2

print(returnCombination(n,k))
