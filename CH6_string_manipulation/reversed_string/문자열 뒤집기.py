from typing import List

def reverseString(s: List[str]) -> None:
    s.reverse()

strs = list(input("입력: "))
reverseString(strs)
print("출력: ", strs)


