from collections import defaultdict

'''

말 그대로 처음 키를 지정할 때 값을 주지 않으면, 해당 키에 대한 값을 디폴트 값을 

지정하겠다는 뜻이다. 


언제 사용하면 좋을까?!

키의 개수를 세야하느 상황이나, 리스트나 셋의 항목을 정리해야 하는 상황에 적절할

'''


#defalultdict 를 사용한 경우

letters = "joojeehwan"

letters_dict = defaultdict(int)


for letter in letters:

    letters_dict[letter] += 1


print(letters_dict)


#defaultdict 를 사용하지 않은 경우


letters = "joojeehwan"

letters_dict = {}

for letter in letters:
    #키가 있는지 확인 하는 작업이 수행 되어야 한다.
    if not letter in letters_dict:
        letters_dict[letter] = 0

    letters_dict[letter] += 1


#리스트나 셋을 활용해서도 여러개의 값을 합칠 때 유용함.

# 주어진 성과 이름 튜플에서 각 성에 대해 어떤 이름들이 있는가 분류하는 것

#이렇게만 하면 중복이 발생하는데
name_list = [("joo", "jeehwan"), ("lee", "jeeyeon"), ("joo", "yoonbal"), ("lee", "choonsoo"), ("kang", "hodong"), ("kang", "hodong")]

ndcit = defaultdict(list)

for key, value in name_list: #리스트의 요소가 튜플이기 때문에, key, value로 할당
    ndcit[key].append(value)

print(ndcit)


#set을 활용하면 중복이 발생하지 않는다.

name_list = [("joo", "jeehwan"), ("lee", "jeeyeon"), ("joo", "yoonbal"), ("lee", "choonsoo"), ("kang", "hodong"), ("kang", "hodong")]

ndcit = defaultdict(set)

for key, value in name_list: #리스트의 요소가 튜플이기 때문에, key, value로 할당
    ndcit[key].add(value)

print(ndcit)




'''
for 루프 안에 if 조건절을 통해서 counter 사전에 어떤 글자가 키(key)로 존재하지 않는 경우, 해당 키에 대한 기본값을 0으로 세팅해주고 있는데요. 
이러한 코딩 패턴은 파이썬에서 사전을 사용할 때 상당히 자주 접할 수 있는데, 코드 가독성 측면에서는 이렇게 사소한 처리가 주요 흐름을 파악을 하는데 방해가 되기도 합니다.
'''
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

'''
파이썬의 내장 모듈인 collections의 defaultdict 클래스는 이러한 경우 사용하면 딱 인데요. defaultdict 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 모든 키에 대해서 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정해줍니다.

먼저, collections 모듈의 defaultdict 클래스는 다음과 같이 임포트해야 합니다.

from collections import defaultdict
이제, 위에서 작성한 코드를 임포트한 defaultdict를 이용해서 개선하면, for 루프로 부터 사전의 기본값 처리 코드를 완전히 제거할 수가 있습니다.
'''

from collections import defaultdict

def countLetters(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter

'''
여기서 defaultdict 클래스의 생성자로 int 함수를 넘긴 이유는 int()는 0을 리턴하기 때문입니다. 
람다 함수를 활용해서 다음과 같이 int 함수 대신에 lambda: 0를 넘겨도 동일하게 작동을 합니다.

'''

from collections import defaultdict

def countLetters(word):
    counter = defaultdict(lambda: 0)
    for letter in word:
        counter[letter] += 1
    return counter