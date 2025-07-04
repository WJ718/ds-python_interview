"""
풀이방법: 
1. 유사 딕셔너리 생성
2. 반복문을 통해 단어 하나하나 팀소트로 정렬, 해당 객체를 키로 값인 리스트에 append
3. 리스트 리턴
"""

from typing import List
import collections

testcase = ["eat", "tea", "tan", "ate", "nat", "bat"]

def grouping(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬된 문자열 : 키
        anagrams[''.join(sorted(word))].append(word)
    
    return list(anagrams.values())

print(grouping(testcase))

