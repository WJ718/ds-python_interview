"""
금지된 단어를 제외하고, 가장 많이 나온 단어를 리턴하라


1. 정규표현식, lower() 메서드로 한 번 조정
2. 금지 단어 제외하고 다른 리스트에 담음
3. Counter메서드로 가장 많이 나온 문자열 출력

(대소문자 구분 X, 구두점 무시)
"""

from collections import Counter
import re

# test case
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = re.findall(r'\w+', paragraph.lower())
filtered = [word for word in words if word not in banned]

# common = 첫 번째로 많이 나온 키 값
common = Counter(filtered).most_common(1)[0][0]
print(common)




