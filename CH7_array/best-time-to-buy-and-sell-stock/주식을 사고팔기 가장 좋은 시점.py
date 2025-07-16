"""
가장 쌀 때 사서 가장 비쌀 때 팔아야 한다. 가장 큰 이익을 출력하라.

testcase = [7,1,5,3,6,4]
output = 5 

방법: 저점을 갱신해가며 현재 값의 차이를 계산
"""
from typing import List

testcase = [7,1,5,3,6,4]

def calcProfit(case: List[int]) -> int:
    profit = 0
    min_price = case[0]

    for c in case:
        min_price = min(min_price, c)
        profit = max(profit, c - min_price)
    
    return profit

print(calcProfit(testcase))


    
        

