"""
괄호로 된 입력값이 올바른지 확인하는 문제
[input]
()[]{}
[output]
true

[접근방법]

입력을 리스트(스택)에 차례차례 집어넣고, 닫는 괄호가 나오면 두 개를 pop해서 짝이 맞는지 확인.
짝이 아닐 시 즉시 break (False)

모두 통과하면 자동적으로 True
"""

table = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}
parentheses = "()[]{}"
stack = []
result = True

for char in parentheses:
    if char not in table:
        stack.append(char)
    elif table[char] != char:
        result = False

print(result)
    
    
    








