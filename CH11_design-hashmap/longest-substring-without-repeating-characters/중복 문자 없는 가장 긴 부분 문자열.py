"""
입력>> "abcabcbb"
출력>> 3


접근방법: enumerate로 슬라이딩 윈도우 사용
(처음부터 계산하면서 중복이 안나오면 가중치+1, 중복이 나오면 그대로)


"""

strs = "abcabcbb"

used = {} # 각 문자가 언제 마지막으로 나타났는지 인덱스를 저장
max_len = start = 0


for idx, char in enumerate(strs):
    if char in used and start <= used[char]:
        # start : 부분 문자열의 시작 인덱스
        start = used[char] + 1
    else:
        max_len = max(max_len, idx - start + 1)

    # 이미 확인된 문자는 계속해서 used에 저장됨 ex) used['a'] = 0 , used['b'] = 1 ...
    used[char] = idx

print(max_len)

