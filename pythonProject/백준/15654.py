''''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열



ex1)
3 1
4 5 2

2
4
5


ex2)
4 2
9 8 7 1

1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8

'''


N , M = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

visited = [False] * N

result = []

def dfs(lev, N, M):

    if lev == M:
        print(' '.join(map(str, result)))

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(lst[i])
            dfs(lev + 1, N, M)
            result.pop()
            visited[i] = False

dfs(0, N, M)
