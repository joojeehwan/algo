#이중 for문 빠져 나오기


a = 0

for x in range(0, 100):
    for y in range(0, 100):
        a = y
        print(a)
        if (a == 20):
            break

print("a는 ", a)

# 첫번 째 반복문은 계속 돈다
# flag를 사용해서! 이중포문을 빠져나가보자!

a = 0
flag = True

for x in range(0, 100):
    for y in range(0, 100):
        a = y
        print(a)

        if a == 20:
            flag = False
            break
    if flag == False:
        break

print("a는 ", a)