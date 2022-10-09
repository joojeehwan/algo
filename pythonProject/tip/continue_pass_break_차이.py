'''


1.     pass : 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행합니다.

2.     continue : 바로 다음 순번의 loop를 수행합니다.

3.     break : 반복문을 멈추고 loop 밖으로 나가도록합니다.


'''


# pass

for i in range(10):
    if i % 2 == 0:
        pass
        print(i)
    else:
        print(i)
print("Done")


'''

0
1
2
3
4
5
6
7
8
9
Done

if문을 사용해서 짝수인 경우와 짝수가 아닌 경우를 나누었습니다.

짝수인경우 pass가 수행된 후 print문이 수행되면서 0~9까지 전부 출력된 것을 확인할 수 있습니다.

즉, 반복문 수행에있어서 전혀 영향을 끼치지 않습니다.

pass가 사용되는 경우는 1. 조건문에서 넣어줄 조건이 딱히 없을경우, 2. class 선언할 때, 초기에 넣어줄 값이 없을 때 정도로 생각할 수 있을 것 같습니다.

일단 코드를 작성한 후 동작 확인을 위해서 실행할 때, 해당 부분에서 오류가 발생하지 않도록 하기위해 많이 사용한답니다.

'''

# continue

for i in range(10):
    if i % 2 == 0:
        continue
        print(i)
    print(i)
print("Done")

'''
1
3
5
7
9
Done

위의 결과를 보면 i가 2의 배수인 경우에는 continue가 실행됩니다.

continue가 실행되면 해당 부분을 그냥 넘어가게됩니다. 

해당 순번의 loop를 넘어가 다음번 loop로 들어가게됩니다. 

따라서 if문 안에 있는 print문과 if문 밖의 print문 둘 다 실행되지 않고 다음 loop로 넘어갑니다.

'''


#break

for i in range(10):
    if i % 2 == 0:
        break
        print(i)
    else:
        print(i)
print("Done")

'''

Done

break 문이 실행되면 해당 반복문을 멈추고 밖으로 나가게됩니다.

위의 예시를 보면 처음 i 는 0 에서부터 시작합니다.

i == 0인 상태에서 조건문이 실행됩니다.

나머지가 0 이므로 if 조건문으로 들어가 break가 실행됩니다.

break에 의해 for문이 종료되고 print("Done")만 실행됩니다.

'''