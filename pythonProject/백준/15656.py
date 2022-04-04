'''

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

4 2
9 8 7 1

1 1
1 7
1 8
1 9
7 1
7 7
7 8
7 9
8 1
8 7
8 8
8 9
9 1
9 7
9 8
9 9
'''

'''
N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(L[i])
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)

'''

def dfs(lev):


    if lev == M:
        print(*lst)
        return

    for i in range(N):
        lst.append(Numbers[i])
        dfs(lev + 1)
        lst.pop()


N, M = map(int, input().split())
Numbers = list(map(int, input().split()))
lst = []
Numbers.sort()

dfs(0)