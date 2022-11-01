# count

'''

[문자열].count(x)
: 문자열 전 범위에서 x가 등장하는 횟수를 반환한다.

[문자열].count(x, start)
: 문자열 start index부터 시작해서 문자열 끝까지 x가 등장하는 횟수를 반환한다.

[문자열].count(x, start, end)
: 문자열 start index부터 시작해서 end index 부분까지의 부분 문자열부터 x가 등장하는 횟수를 반환한다.


'''


s = 'banana'


print(s.count('a'))             # 3
print(s.count('a', 2))          # 2
print(s.count('a', 2, 4))       # 1


# find / index

'''

find 함수는 문자열 내부에 특정 문자가 존재하는지 확인하고, 존재하는 위치의 index를 반환해준다.

find

문자열 내부에 특정 문자가 존재하지 않은 경우에는 -1을 반환한다!
찾는 문자가 여러 개 존재할 경우, 맨 처음 인덱스를 반환한다.

[문자열].find(x)
: 문자열 전 범위에서 x가 존재하는 인덱스를 반환한다.

[문자열].find(x, start)
: 문자열 start index 부분부터 시작해서 문자열 끝까지 x가 존재하는 인덱스를 반환한다.

[문자열].find(x, start, end)
: 문자열 start index 부분부터 end index 부분까지의 부분 문자열에서 x가 존재하는 인덱스를 반환한다.

📌 rfind

추가적으로 찾고 싶은 문자가 여러 개일 때 마지막 인덱스를 반환해주고 싶을 경우 rfind를 사용하면 된다!
사용법은 find 함수와 동일하다.


📌 rindex

rfind처럼 찾고 싶은 문자가 여러 개일때 마지막 인덱스를 반환해준다.

📌 find와 index의 차이

1. 찾는 문자가 없을 때
find: -1을 반환한다.
index: ValueError 에러가 발생한다.
2. 자료형
find: 문자열만 사용 가능하다. 리스트, 튜플, 딕셔너리 자료형에서는 사용하면 AttributeError 에러가 발생한다.
index: 문자열, 리스트, 튜플 자료형에서 사용 가능하다. 딕셔너리 자료형에서는 사용할 수 없어 AttributeError 에러가 발생한다.

'''


s = 'banana'

print(s.find('a'))             # 1
print(s.find('a', 2))          # 3
print(s.find('a', 4, 6))       # 5


#upper, lower, swapcase

'''
[문자열].upper()
: 문자열의 모든 문자를 대문자로 바꿔준다.

[문자열].lower()
: 문자열의 모든 문자를 소문자로 바꿔준다.

[문자열].swapcase()
: 문자열의 소문자는 대문자로, 대문자는 소문자로 서로 바꿔준다.



'''

s = 'Hello World'

print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world
print(s.swapcase())     # hELLO wORLD


#strip, lstrip, rstrip

'''

[문자열].lstrip()
: 기존 문자열에 있는 왼쪽 공백을 제거한 문자열을 반환한다.

[문자열].rstrip()
: 기존 문자열에 있는 오른쪽 공백을 제거한 문자열을 반환한다.

[문자열].strip()
: 기존 문자열에 있는 양쪽 공백을 제거한 문자열을 반환한다.
'''


s = '    Hello World    '

print('<' + s.lstrip() + '>')       # <Hello World    >
print('<' + s.rstrip() + '>')       # <    Hello World>
print('<' + s.strip() + '>')        # <Hello World>




#join

'''
join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환해준다.

''.join(리스트)
: 매개변수로 들어온 리스트를 문자열로 합쳐서 반환해준다.

'[구분자]'.join(리스트)
: 리스트의 값과 값 사이에 구분자에 들어온 구분자를 넣어서 하나의 문자열로 합쳐서 반환한다.



'''


numbers = ['1', '2', '3']

print(''.join(numbers))     # 123
print(', '.join(numbers))   # 1, 2, 3




#replace

'''
replace 함수는 기존의 문자열의 요소를 원하는 문자로 바꿀 때 사용한다.

[문자열].replace(old, new)
: 기존 문자에 있는 old 문자를 new 문자로 변경해서, 그 변경한 문자열을 반환한다.

[문자열].replace(old, new, count)
: 해당 문자가 여러 개 존재할 때, 일부만 변경하고 싶을 때 사용한다. 기존 문자에 있는 old 문자를 new 문자로 count 개수만큼만 변경해서, 그 변경한 문자열을 반환한다.

📌 주의

replace를 한 뒤, 원본 문자열은 변경되지 않는다!
'''

s = 'Hello Python'

print(s.replace('Python', 'Yeonju'))    # Hello Yeonju
print(s.replace('o', 'i', 1))           # Helli Python

#split

'''

split 함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어 주는 함수이다.


[문자열].split()
: 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나눈다.

[문자열].split(구분자)
: 구분자를 기준으로 문자열을 나눈다.

[문자열].split(구분자, 분할 횟수)
: 구분자를 기준으로 분할 횟수만큼 문자열을 나눈다.
'''

s = 'abc, de, f, g'

print(s)                # abc, de, f, g
print(s.split())        # ['abc,', 'de,', 'f,', 'g']
print(s.split(','))     # ['abc', ' de', ' f', ' g']