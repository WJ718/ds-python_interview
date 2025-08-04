"""
2 = abc
3 = def
4 = ghi
5 = jkl
6 = mno
7 = pqrs 
8 = tuv
9 = wxyz

2~9까지 주어졌을 때 조합 가능한 모든 문자열을 리스트에 넣어서 출력. 

**접근방식**

순서를 상관하지 않으므로, itertools.product 모듈 사용하기

[도움받은 부분] - product 사용법. ex) product(['a','b','c'], ['d','e','f']) 식으로 사용

1. 튜플에 숫자:문자열 리스트 형태로 저장
2. 튜플 속에 입력한 숫자가 있는지 확인하고, 값만 새로운 리스트에 저장
3. 값이 들어있는 리스트를 요소로 itertools.product 연산을 수행한 요소를 또 다른 리스트에 저장해 반환


시간복잡도: O(n * 4^n)
공간복잡도: O(n & 4^n)
n = 입력된 문자열 길이
"""
import itertools

def combination(digits):
    keypad = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z'],
    }

    # 입력된 각 숫자를 키패드의 리스트로 매핑 (list comprehension)
    letters = [keypad[d] for d in digits if d in keypad]
    # letters의 각 요소를 product하고, 그 결과들을 하나씩 새로운 리스트에 추가해 반환
    return [''.join(tup) for tup in itertools.product(*letters)]

print(combination("23"))