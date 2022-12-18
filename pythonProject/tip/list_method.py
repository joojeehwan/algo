'''

리스트 자료 형은 몇 가지 메서드들을 더 갖고 있습니다. 이것들이 리스트 객체의 모든 메서드 들입니다:

list.append(x)
리스트의 끝에 항목을 더합니다. a[len(a):] = [x] 와 동등합니다.

list.extend(iterable)
리스트의 끝에 이터러블의 모든 항목을 덧붙여서 확장합니다. a[len(a):] = iterable 와 동등합니다.

list.insert(i, x)
주어진 위치에 항목을 삽입합니다. 첫 번째 인자는 삽입되는 요소가 갖게 될 인덱스입니다. 그래서 a.insert(0, x) 는 리스트의 처음에 삽입하고, a.insert(len(a), x) 는 a.append(x) 와 동등합니다.

list.remove(x)
리스트에서 값이 x 와 같은 첫 번째 항목을 삭제합니다. 그런 항목이 없으면 ValueError를 일으킵니다.

list.pop([i])
리스트에서 주어진 위치에 있는 항목을 삭제하고, 그 항목을 돌려줍니다. 인덱스를 지정하지 않으면, a.pop() 은 리스트의 마지막 항목을 삭제하고 돌려줍니다. (메서드 시그니처에서 i 를 둘러싼 대괄호는 매개변수가 선택적임을 나타냅니다. 그 위치에 대괄호를 입력해야 한다는 뜻이 아닙니다. 이 표기법은 파이썬 라이브러리 레퍼런스에서 지주 등장합니다.)

list.clear()
리스트의 모든 항목을 삭제합니다. del a[:] 와 동등합니다.

list.index(x[, start[, end]])
리스트에 있는 항목 중 값이 x 와 같은 첫 번째 것의 0부터 시작하는 인덱스를 돌려줍니다. 그런 항목이 없으면 ValueError 를 일으킵니다.

선택적인 인자 start 와 end 는 슬라이스 표기법처럼 해석되고, 검색을 리스트의 특별한 서브 시퀀스로 제한하는 데 사용됩니다. 돌려주는 인덱스는 start 인자가 아니라 전체 시퀀스의 시작을 기준으로 합니다.

list.count(x)
리스트에서 x 가 등장하는 횟수를 돌려줍니다.

list.sort(*, key=None, reverse=False)
리스트의 항목들을 제자리에서 정렬합니다 (인자들은 정렬 커스터마이제이션에 사용될 수 있습니다. 설명은 sorted() 를 보세요).

list.reverse()
리스트의 요소들을 제자리에서 뒤집습니다.

list.copy()
리스트의 얕은 사본을 돌려줍니다. a[:] 와 동등합니다.

'''

'''
List
List 자료형은 저장되는 데이터가 서로 다른 형태의 데이터여도 저장되며, 변경 가능하다는 점 때문에 데이터 분석에서 많이 사용된다.
튜플은 자료 갱신이 안된다.

List Method
del : 삭제

'''

list_1 = ['abc', 123, 3.14, ['edf', 456], ('gh', 'st')]

print(list_1)

# ['abc', 123, 3.14, ['edf', 456], ('gh', 'st')]

del list_1

print(list_1)
'''
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

NameError: name 'list_1' is not defined
'''

'''


'''

'''

기본 연산자
리스트의 기본 연산자에는 리스트 길이는 재는 len() 함수, 
리스트를 합치는 + 연산자, 
리스트 값을 반복하는 * 연산자, 
포함 여부 값(True, False)을 반환하는 in 연산자, 
함수를 반복하는데 사용하는 for loop 문 등이 있다.

'''

len([1, 2, 3])	#3
[1, 2, 3] + [4, 5, 6]	#[1, 2, 3, 4, 5, 6]
[1, 2, 3] * 3	[1, 2, 3, 1, 2, 3, 1, 2, 3]
1 in [1, 2, 3] #True
4 in [1, 2, 3] #False
for i in [1, 2, 3]:
    print(i)

'''
List 내장 함수
함수	설명
len(list)	리스트 길이
max(list)	리스트 내 최대 요소
min(list)	리스트 내 최소 요소
list(seq)	리스트로 변환
len(list) : 리스트 길이

'''

## len(list) : 리스트 길이
list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

print(len(list_a))
# 5

print(len(list_b))
# 6

## max(list) : 리스트 내 최대 요소(문자인 경우 알파벳 순서 기준)
list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

print(max(list_a))
# 5

print(max(list_b))
# o

## min(list) : 리스트 내 최소 요소(문자인 경우 알파벳 순서 기준)

list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

print(min(list_a))
# 1

print(min(list_b))
# g

## list(seq) : 리스트로 변환

tuple_a = ('gil', 'log')

print(type(tuple_a))
#<class 'tuple'>

list_tuple = list(tuple_a)

print(type(list_tuple))
#<class 'list'>


### Python List Method

## append(obj) : 기존 리스트에 1개 데이터 추가(2개 이상 불가)

list_a = [1, 2, 3, 4, 5]

list_a.append(6)

print(list_a)
# [1, 2, 3, 4, 5, 6]

## extend(seq) : 기존 리스트에 다른 리스트 이어 붙이기
list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

list_a.extend(list_b)

print(list_a)
# [1, 2, 3, 4, 5, 6, 'g', 'i', 'l', 'l', 'o', 'g']

## count(obj) : 리스트 안에 obj가 몇 개 들어 있는지 개수 반환
list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

print(list_a.count(5))
# 1

print(list_b.count('l'))
# 2

## index(obj) : 리스트 에서 obj가 있는 가장 작은 index 반환
#list 안에 없는 obj를 인자로 넣고 실행 시키면 ValueError가 발생한다.

list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

print(list_a.index(4))
# 3

print(list_b.index('l'))
# 2

## insert(index, obj) : 리스트의 index 위치에 obj 값 삽입
list_a = [1, 2, 3, 4, 5]

list_a.insert(3, 45)

print(list_a)
# [1, 2, 3, 45, 4, 5]

## pop() : 리스트의 마지막 요소 제거 및 반환
#인자로 index 위치 정수를 입력하면 해당 index의 요소를 제거 후 반환 한다.

list_a = [1, 2, 3, 4, 5]

print(list_a.pop())
# 5

print(list_a)
# [1, 2, 3, 4]

print(list_a.pop(2))
# 3

print(list_a)
# [1, 2, 4]

## remove(obj) : 리스트에서 obj 객체 제거(1개 인자만 가능, 2개 이상 TypeError 발생)
list_b = ['g', 'i', 'l', 'l', 'o', 'g']

list_b.remove('l')
# ['g', 'i', 'l', 'o', 'g']

## reverse() : 리스트의 객체들 순서 반대로 뒤집기
list_b = ['g', 'i', 'l', 'l', 'o', 'g']

list_b.reverse()

print(list_b)
# ['g', 'o', 'l', 'l', 'i', 'g']


## sort() : 리스트의 객체들 순서대로 정렬(오름차순)

'''
숫자와 문자가 섞여있는 list에서는 sort()를 실행 할 경우 TypeError가 발생한다.

한 종류로 이루어진 list에서만 실행 가능한 method 이다.

내림차순으로 정렬하고 싶다면 sort(reverse=True)로 인자에 reverse=True를 입력해주면 된다.

'''


list_a = [1, 2, 3, 4, 5]

list_b = ['g', 'i', 'l', 'l', 'o', 'g']

# 파이썬 리스트 메소드

list_b.sort()

print(list_b)
# ['g', 'g', 'i', 'l', 'l', 'o']

list_a.sort(reverse=True)

print(list_a)
#[5, 4, 3, 2, 1]