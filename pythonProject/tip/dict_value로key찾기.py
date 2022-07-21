'''

2가지 방법 제시


1. dict를 뒤집어서 key와 value의 자리를 바꾼다.

2. for문을 활용한다.
'''


#1
pratice_dict = {}
pratice_dict['삼성전자'] = '005930'
pratice_dict['카카오'] = '035720'
pratice_dict['현대차'] = '005380'
print(pratice_dict)

revers_dict = dict(map(reversed, pratice_dict.items()))
print(revers_dict)

#2


for key, value in pratice_dict.items():
    if value == "005930":
        print(key)

my_dict = {"John": 1, "Michael": 2, "Shawn": 3}


#함수화
def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "There is no such Key"


print(get_key(1))
print(get_key(2))