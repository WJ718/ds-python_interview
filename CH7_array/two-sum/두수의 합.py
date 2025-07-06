from typing import List

nums = [2,7,11,15]
target = 9

def twoSum(nums : List[int], target) -> List[int]:
    nmap = {}

    for i , num in enumerate(nums):
        # 숫자(키)에 따른 인덱스를 값으로 저장
        nmap[num] = i

    # 목표에서 배열의 왼쪽 숫자부터 빼가며 딕셔너리에 합이 되는 수가 있는지 확인  
    for i , num in enumerate(nums):
        # target - num이 키인 값이 있으면서, 같은 인덱스를 쓰는 경우가 아니라면
        if target - num in nmap and i != nmap[target-num]:
            # 결과를 반환
            return [i, nmap[target-num]]
        
answer = twoSum(nums,target)
print(answer)