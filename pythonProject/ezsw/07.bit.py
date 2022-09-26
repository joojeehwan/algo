

'''
원소가 n개인 집합

부분 집합의 총 개수 -> 1 << n


i 번쨰 원소가 있는 지 확인

* (비트로 표현된 집합) & (1 << i) 결과가 0이 아니면 존재
* e.g. 2번 째 원소가 있는지 확인

    0101 & (1 << 2) = 0101 & 0100 = 0100


i 번쨰 원소를 추가

* (비트로 표현된 집합) | (1 << i)
* e.g. 1번 째 원소를 추가

    0101 | (1 << 1) = 0101 | 0010 = 0111

i 번쨰 원소를 삭제

* (비트로 표현된 집합) & ~(1 << i)
* e.g. 2번 째 원소를 삭제

    0101 & ~(1 << 2) = 0101 & ~(0100) = 0101 & 1011 = 0001



'''


def printSubsets(arr, n):

    for i in range(1 << n):

        print("{", end = " ")

        for j in range(n):
            if i & (1 << j):
                print(arr[j], end = " ")

        print("}")

lst = ['A', 'B', 'C', 'D']
print(printSubsets(lst, 4))


'''

집합의 원소 개수 구하기 


'''

# 빌트인 함수 활용

n = 4

bin(n).count(1)

#자체 구현

def countBits(n):

    ret = 0
    while n:
        if n & 1:
            ret += 1
        n = n >> 1

    return ret

'''

부분 집합 연습 - 두 수의 합이 7인 경우의 수 

입력

6 
1 2 3 4 5 6 

'''

def solve():
    ret = 0
    for i in range(1 << N):
        if bin(i).count('1') != 2:
            continue

        sum = 0
        for j in range(N):
            if i & (1 << j):
                sum += lst[j]

        if sum == 7:
            ret += 1

    return ret


N = int(input())
lst = list(map(int, input().split()))
print(solve())

