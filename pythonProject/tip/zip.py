'''



zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다.
'''


# zip version
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

'''

(1, 'A')
(2, 'B')
(3, 'C')

'''

#그냥 인덱스 변수 사용


numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for i in range(3):
     pair = (numbers[i], letters[i])
     print(pair)

'''
(1, 'A')
(2, 'B')
(3, 'C')

'''

#응용 0번 - 사전 변환 ** 이걸 가장 많이 사용 **

'''

zip() 함수를 이용하면 두 개의 리스트나 터플 부터 쉽게 사전(dictionary)을 만들 수 있습니다. 
키를 담고 있는 리스트와 값을 담고 있는 리스트를 zip() 함수에 넘긴 후, 그 결과를 다시 dict() 함수에 넘기면 됩니다.

'''

keys = [1, 2, 3]
values = ["A", "B", "C"]
dict(zip(keys, values))
#{1: 'A', 2: 'B', 3: 'C'}

#응용 1번 - 병렬 처리

'''
zip() 함수를 활용하면 여러 그룹의 데이터를 루프를 한 번만 돌면서 처리할 수 있는데요. 가변 인자를 받기 때문에 2개 이상의 인자를 넘겨서 병렬 처리를 할 수 있습니다.

예를 들어, 아래 코드는 3개의 문자열 내의 글자를 하니씩 병렬해서 출력하고 있습니다.

'''

for number, upper, lower in zip("12345", "ABCDE", "abcde"):
     print(number, upper, lower)


'''

1 A a
2 B b
3 C c
4 D d
5 E e

'''


#응용 2번 - unzip

numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))
print(pairs)

#[(1, 'A'), (2, 'B'), (3, 'C')]

'''

이 리스트 앞에 풀기(unpacking) 연산자 붙여서 다시 zip() 함수에 넘기면 다시 원래의 2개의 터플을 얻을 수 있습니다.

'''

numbers, letters = zip(*pairs)

print(numbers)
# (1, 2, 3)
print(letters)
# ('A', 'B', 'C')


# 주의

'''
zip() 함수로 넘기는 인자의 길이가 다를 때는 주의를 해야 합니다. 왜냐하면 가장 짧은 인자를 기준으로 데이터가 엮이고, 나머지는 버려지기 때문입니다.

'''
numers = ["1", "2", "3"]
letters = ["A"]
list(zip(numbers, letters))
#[('1', 'A')]



