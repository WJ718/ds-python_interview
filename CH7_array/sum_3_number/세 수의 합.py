from typing import List

testcase = [-1,0,1,2,-1,-4]

def calc(t: List[int]) -> List[int]:
    result = []
    sum = 0
    # 오름차순 정렬
    t.sort()    

    # 세 수의 합을 구해야 하므로 첫 수는 끝에서 2를 뺀 것까지가 최대
    for i in range(len(t) - 2):

        # 중복 제거
        if i > 0 and t[i] == t[i-1]:
            continue

        # 간격 좁혀가며 합 구함
        left, right = i+1, len(t)-1
        
        while left < right:
            sum = t[i] + t[left] + t[right]
        
            # 합이 0보다 작다 -> 왼쪽 포인터 오른쪽으로 이동
            if sum < 0:
                left += 1
            # 합이 0보다 크다 -> 오른쪽 포인터 왼쪽으로 이동 
            elif sum > 0:
                right -= 1

            # 합이 0일 시
            else:
                # 결과 리스트에 저장 후 남은 부분 추가 계산
                result.append([t[i], t[left], t[right]])

                # 같은 값이 있다면 건너 뛰기 (결과가 중복되니깐)
                while left < right and t[left] == t[left + 1]: 
                    left += 1
                while left < right and t[right] == t[right - 1]:
                    right -= 1

                # 양쪽 포인터 이동
                left += 1
                right -= 1

    return result

answer = calc(testcase)
print(answer)

