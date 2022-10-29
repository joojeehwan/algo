'''


len 함수는 매개변수로 들어온 문자열의 길이 를 반환합니다.
즉, 내부에 있는 문자의 개수(공백포함)을 계산해서 반환해주는 함수입니다.

'''

name = 'BlockDMask'
phone = '010 xxxx xxxx'
address = 'korea'

print(len(name))  # 10
print(len(phone))  # 13
print(len(address))  # 5


# =====================================
# len 예제 2.
# 문자열의 길이를 판단해야하는 경우가 있다고 하면 이런식으로 쓰이겠죠?
def check_name(s):
    if len(s) <= 0:
        print('이름은 1글자 이상 입력해야합니다.')
    else:
        print('좋은 이름 입니다.')


krName1 = ''
krName2 = '고길동'

check_name(krName1)
check_name(krName2)


'''
count 함수는 문자열에서 쓰이는 메서드
문자열 내부에서 특정 문자, 혹은 문자열이 포함 되어있는지 계산해서 반환해주는 함수 입니다.

'''
# 문자열 'BlockDMask' 선언
a = 'BlockDMask'

# 문자열에서 'k'가 몇개 있는지 ?
print('#1 a.count("k")')
print(a.count('k'))

# 문자열에서 'DM'가 몇개 있는지 ?
print('#2 a.count("DM")')
print(a.count('DM'))

# 문자열에서 특정 범위 내부에 'k' 가 몇개 있는지?
# B l o c k D M a s k 에서 index를 표기해보면
# 0 1 2 3 4 5 6 7 8 9 입니다.

print("#3 a[2] + ' ~ ' + a[4]")
print(a[2] + ' ~ ' + a[4])

print("#4 a.count('k', 2, 3)")
print(a.count('k', 2, 3))

print("#5 a.count('k', 2, 4)")
print(a.count('k', 2, 4))

print("#6 a.count('k', 2, 5)")
print(a.count('k', 2, 5))



from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue']) # 3
print(counter['green']) # 1
print(dict(counter)) # 딕셔너리로 변환
# {'red' : 2, 'blue': 3, 'green': 1}
