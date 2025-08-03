"""
[input]
bcabc
[output]
abc

중복된 문자를 제거하고, 사전순으로 정렬해서 출력

하나하나 살피며 테이블 기록, 동시에 테이블에서 중복 발견 시 stack에 저장 x
마지막에 스택에 저장된 문자들 문자열로 바꾼 후 팀소트로 정렬

"""

testcase = "bcabc"
table = {}
stack = []

for char in testcase:
    if char not in table:
        table.update({char : True})
        stack.append(char)

stack.sort()

result = ''.join(stack)
print(result)

