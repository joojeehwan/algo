'''


1 ) 의미 익명함수를 지칭하는 용어 즉, 기존의 함수(명 등)을 선언하고
사용하던 방식과는 달리 바로 정의하여 사용할 수 있는 함수.



2 ) 형식 : lambda 인자 : 표현식 예시) sum = lambda x: x+1



3 ) 인자 넣기 : 람다 표현식을 괄호로 묶은 뒤에 다시 괄호를 붙이고 인수를 넣어 호출

(lambda x: x + 10)(1)
> 11

4 ) 인자 두 개 쓰기 : lambda x,y: x+y



5 ) if 사용하기

check_pass = lambda x: 'pass' if x>=70 else 'fail'

'''





'''
리스트를 정렬 key 사용
'''
data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

#중복 제거
data_list = list(set(data_list))

data_list.sort()
data_list.sort(key=lambda x : len(x))

print(data_list)


e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]

#첫번 째 인자 오름차순, 두 번째 인자 내림차순
f = sorted(e, key = lambda x : (x[0], -x[1]))


s = ['2 A', '1 B', '4 C', '1 A']
s.sorted(s, key=lambda x: (x.split()[1], x.split()[0]))

'''
map 람다 표현식
'''
list(map(lambda x: x+10, [1,2,3]))
# [11, 12, 13]



'''
filter
'''

a = [8, 4, 2, 5, 2, 7, 9, 11, 26, 13]

result = list(filter(lambda x : x > 7 and x < 15, a))
