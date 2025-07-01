import re

strs = input()
strs = re.sub('[^a-z0-9]', '', strs)
answer = True

if strs != strs[::-1]: # not a palindrome
    answer = False

print(answer)










