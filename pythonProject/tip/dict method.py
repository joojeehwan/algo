'''

'순서와 중복을 허용하지 않는다'가 파이썬 Dictionary의 가장 큰 특징입니다.


'''

#사전 생성

a = { "name": "사용자", "email": "user@test.com", "age": 25 }

b = {}

c = dict()

d = dict(name="사용자", email="user@test.com", age=25)

e = dict([("name", "사용자"), ("email", "user@test.com"), ("age", 25)])


# fromkeys

'''

dict.fromkeys(seq, value)
딕셔너리를 생성할 때 편리하게 사용할 수 있는 메소드. seq 옵션 값에 문자열을 입력할 수도 있다.
seq: 생성하려는 dictionary의 키(key)의 목록
value: 생성하려는 dictionary의 값(value)

'''

seq = ('name', 'age', 'sex')

dict_1 = dict.fromkeys(seq)
print(dict_1)

dict_2 = dict.fromkeys(seq, 10)
print(dict_2)

## result ##
#{'age':None, 'name':None, 'sex':None}
#{'age':10, 'name':10, 'sex':10}

# 데이터 추가

'''
사전에 데이터를 추가할 때는 대괄호([<키>] = <값>)를 사용하여 원하는 값을 할당해주면 됩니다.
'''

user = {}
user["name"] = "사용자"
user["email"] = "user@test.com"
user["age"] = 25
# {'name': '사용자', 'email': 'user@test.com', 'age': 25}

# 데이터 접근

print(user["name"])
#'사용자'
print(user["email"])
#'user@test.com'
print(user["age"])
#25


'''
한 가지 주의할 점은 사전에 존재하지 않는 키를 사용하면 KeyError 오류가 발생한다는 것입니다.

>>> user["mail"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'mail'
이러한 오류를 방지하고 싶다면, get(<키>[, <기본값>]) 메서드를 사용하면 됩니다. 기본값을 지정해주지 않으면, 키가 존재하지 않을 때, None을 반환합니다.

'''
print(user.get("mail", "서울"))
#'서울'
print(user.get("mail"))
#None

#데이터 갱신

'''
가변 데이터 타입인 사전은 자유롭게 담고 있는 데이터를 갱신할 수 있습니다. 기존 키에 새로운 값을 할당하기만 하면 기존 값이 새로운 값으로 대체됩니다.
'''
user["age"] = 31
print(user)
#{'name': '사용자', 'email': 'user@test.com', 'age': 31}


#데이터 삭제

'''
del 키워드를 사용해서 특정 키와 값의 쌍을 사전에서 제거할 수 있습니다.

Remove all items from a dictionary: clear()
Remove an item by a key and return a value: pop()
Remove an item and return a key and value: popitem()
Remove an item by a key from a dictionary: del
Remove items that meet the condition: Dictionary comprehensions

'''

## del
del user["email"]
print(user)
#{'name': '사용자', 'age': 31}

d = {'k1': 1, 'k2': 2, 'k3': 3}


## clear()
d.clear()
print(d)
# {}

## pop()

d = {'k1': 1, 'k2': 2, 'k3': 3}

removed_value = d.pop('k1')
print(d)
# {'k2': 2, 'k3': 3}

print(removed_value)
# 1

#By default, specifying a non-existent key raises KeyError.

d = {'k1': 1, 'k2': 2, 'k3': 3}

# removed_value = d.pop('k4')
# print(d)
# KeyError: 'k4'

'''

source: dict_clear_pop_popitem_del.py
If the second argument is specified, its value is returned if the key does not exist. The dictionary itself remains unchanged.

'''

d = {'k1': 1, 'k2': 2, 'k3': 3}

removed_value = d.pop('k4', None)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

print(removed_value)
# None


## popitem()

'''

The popitem() method removes an item from a dictionary and returns a tuple of its key and value (key, value). You cannot specify which item to remove.

An error KeyError is raised for an empty dictionary.

'''

d = {'k1': 1, 'k2': 2}

k, v = d.popitem()
print(k)
print(v)
print(d)
# k2
# 2
# {'k1': 1}

k, v = d.popitem()
print(k)
print(v)
print(d)
# k1
# 1
# {}

# k, v = d.popitem()
# KeyError: 'popitem(): dictionary is empty'


## Remove items that meet the condition: Dictionary comprehensions

'''
To remove items that satisfy the conditions from a dictionary, use dictionary comprehensions, the dictionary version of list comprehensions.

List comprehensions in Python
"Removing items that meet the condition" is the same as "extracting items that do not meet the condition".

For example, to remove items with an odd value, you can extract items with an even value. The same applies to the opposite case.

'''

d = {'apple': 1, 'banana': 10, 'orange': 100}

dc = {k: v for k, v in d.items() if v % 2 == 0}
print(dc)
# {'banana': 10, 'orange': 100}

dc = {k: v for k, v in d.items() if v % 2 == 1}
print(dc)
# {'apple': 1}


'''

The items() method of dict is used to extract keys and values.

Iterate dictionary (key and value) with for loop in Python
It is also possible to specify conditions for keys.


'''

dc = {k: v for k, v in d.items() if k.endswith('e')}
print(dc)
# {'apple': 1, 'orange': 100}

dc = {k: v for k, v in d.items() if not k.endswith('e')}
print(dc)
# {'banana': 10}

'''

You can also use and and or to specify multiple conditions.

Boolean operators in Python (and, or, not)


'''

dc = {k: v for k, v in d.items() if v % 2 == 0 and k.endswith('e')}
print(dc)
# {'orange': 100}


#데이터 순회

'''
in 연산자를 통해서 사전에 있는 모든 데이터를 for 루프문으로 순회할 수 있습니다. 기본적으로는 키만 얻어지기 때문에, 값은 대괄호를 이용해서 접근해야 합니다.
'''

user = {"name": "사용자", "email": "user@test.com", "age": 25}
for key in user:
    print(f"{key}: {user[key]}")



'''
하지만 items() 메서드를 활용하면 키와 값을 터플의 형태로 한 번에 얻을 수 있어서 좀 더 깔끔하게 루프문을 작성할 수 있습니다.
'''

user = {"name": "사용자", "email": "user@test.com", "age": 25}
for key, value in user.items():
     print(f"{key}: {value}")

'''
name: 사용자
email: user@test.com
age: 25
'''

#특정키 존재 확인

user = {"name": "사용자", "email": "user@test.com", "age": 25}
print("email" in user)
#True
print("mail" in user)
#False

'''
따라서 if 조건문과도 자연스럽게 함께 사용할 수 있습니다.
'''


if "email" in user:
    print("email 키는 존재합니다.")
else:
    print("email 키를 사전에서 찾을 수 없습니다.")


# 사전 병합

'''
여러 개의 사전을 합쳐야할 때는 ** 연산자를 사용하여, 중괄호 안에 합칠 사전들을 쉼표(,)로 구분하여 나열하면 됩니다.
'''
dic1 = {"A": 1, "B": 2}
dic2 = {"B": 3, "C": 4}
new_dic = { **dic1, **dic2 }
print(new_dic)
#{'A': 1, 'B': 3, 'C': 4}

#Python 3.9 버전부터는 대신에 | 연산자를 사용해서 좀 더 깔끔하게 여러 개의 사전을 병합할 수 있습니다.

new_dic = dic1 | dic2
print(new_dic)
#{'A': 1, 'B': 3, 'C': 4}


# 사전 반영

'''
하나의 사전에 다른 사전의 모든 데이터를 반영하고 싶을 때는 사전의 update() 메서드를 사용할 수 있습니다.
단순 병합과 달리 다른 사전에 데이터가 반영되면서 기본 사전에 있는 데이터가 변경되는 부분 주의 바라겠습니다.
'''

dic1 = {"A": 1, "B": 2}
dic2 = {"B": 3, "C": 4}
dic1.update(dic2)
print(dic1)
#{'A': 1, 'B': 3, 'C': 4}


#마찬가지로 Python 3.9 버전에서 사전에 추가된 | 연산자를 활용해서 같은 효과를 낼 수도 있습니다.

dic1 = {"A": 1, "B": 2}
dic2 = {"B": 3, "C": 4}
dic1 |= dic2
print(dic1)
#{'A': 1, 'B': 3, 'C': 4}



