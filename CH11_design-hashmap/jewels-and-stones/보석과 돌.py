"""
입력> J = "aA", S = "aAAbbbb"
출력> 3

[접근방식]
1. S의 요소들을 해시테이블에 저장하고, 보석의 조건이 되는 갯수를 더함 (가장 코드 수 많음)
2. Counter 사용해서 계산 생략하기
"""
import collections

J = "aA"
S = "aAAbbbb"

freqs = collections.Counter(S) # S의 빈도 수 계산
count = 0

# J의 빈도 수 합산
for char in J:
        count += freqs[char]

print(count)

