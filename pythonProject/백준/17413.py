'''

단어 뒤집기 2



문자열 s가 주어졌을 때, "단어"만 뒤집는다.


'''

#스택을 활용한 풀이

'''
단어들을 stack에 담고, 이 단어들만 뒤집는다. 

'''
ans = ""
tag = False
stack = ""
lst = input()

for i in lst:

    if i == "<":
        tag = True
        #stack에 있는 것을 전체를 거꾸로 가져오기
        ans += stack[::-1]
        stack = ""
        ans += i
        continue

    elif i == ">":
        tag = False
        ans += i
        continue

    elif  i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue

    if tag:
        ans += i

    else:
        stack += i

print(ans+stack[::-1])

import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))