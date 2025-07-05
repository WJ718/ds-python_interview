"""
어떤 문자열이 주어질 때, 가장 긴 팰린드롬인 부분을 찾는 문제

방법 1: 동적배열을 사용하기 -- 공간복잡도, 시간복잡도 느림
방법 2: 투 포인터를 사용해 비교하기 -- 직관적, 빠름

"""

testcase = "babad"

def find(strs: str) -> str:
    # 범위 확장 메서드
    def expand(left: int, right: int) -> str:
        # 좌우로 팰린드롬 확장
        while left >= 0 and right < len(strs) and strs[left] == strs[right]:
            left -= 1
            right += 1
        
        return strs[left + 1:right]

    # 예외 처리 - 문자 / 이미 회문인 경우 계산 없이 답 리턴
    if len(strs) < 2 or strs == strs[::-1]:
        return strs

    result = ''
    
    # 문자열 오른쪽으로 이동하며 팰린드롬 탐색
    for i in range(len(strs) - 1):
        result = max(result, 
                     expand(i, i+1), # 짝수 길이 중심
                     expand(i, i+2), # 홀수 길이 중심
                     key = len) # 비교 기준 : 문자열길이

    return result

print(find(testcase))