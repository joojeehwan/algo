#마법사 상어와 복제 다시 보기 


'''


for문과 같이 사용되는 else문은
for문이 break 등으로 중간에 빠져나오지 않고
끝까지 실행 됐을 경우 else문이 실행되는 방식으로 진행됩니다.

'''

for i in range(5):
    print(i, end=' ')
else:
    print("for문이 끝까지 실행됬습니다!")

for i in range(5):
    if i == 2:
        break
    print(i, end=' ')
else:
    print("for문이 끝까지 실행됬습니다!")


'''

while_else

while에서 else 구문은 조건이 거짓이 되었을 때 실행된다.
'''

n = 1
while n < 10:
    print(f'{n}은 10 보다 작은 수 입니다.')
    n += 1
else:
    print(f'{n}은 10 이상의 숫자이므로 while을 종료합니다.')
