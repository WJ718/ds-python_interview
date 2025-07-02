"""
- 로그 파일 재정렬 -

1. 로그의 가장 앞 부분은 식별자이다 (dig2, let1)
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
3. 문자의 경우 알파벳순으로 정렬되고, 문자가 동일한 경우 식별자 순서로 정렬된다
4. 숫자 로그는 입력한 순서대로 정렬된다


--> 람다로 분류하고 두 개의 리스트를 더하기

1. 입력된 리스트의 요소 하나하나 숫자인지 문자인지 판별 (공백 기준으로 두 번째 요소가 문자인지 숫자인지 판별 -- isdigit())
2. 분류한 것을 문자가 먼저 오도록 합침

"""
from typing import List

def sortingLogs(logs: List[str]) -> List[str]:
    # create new lists (digit or letter)
    letters, digits = [], [] 

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1: ], x.split()[0]))
    return letters + digits

# test case
strs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
answer = sortingLogs(strs)
print(answer)






