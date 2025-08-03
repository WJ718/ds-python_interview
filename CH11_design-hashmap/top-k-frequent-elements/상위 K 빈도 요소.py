"""
[input]
nums = [1,1,1,2,2,3] , k = 2

[output]
[1,2]

[접근방법]
Counter 사용, 빈도가 2이상인 것들만 새로운 리스트에 넣어서 출력하기
"""
import collections

nums =  [1,1,1,2,2,3]
k = 2

# 결과로 출력할 리스트
result = []

freqs = collections.Counter(nums)

for nums, item in freqs.items():
    if item >= 2:
        result.append(nums)

print(result)




