
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

4 2

1 2
1 3
1 4
2 3
2 4
3 4
'''
n, m  = list(map(int, input().split()))
s = []

def dfs(start):

    if len(s) == m:
        print(" ".join(map(str, s)))
        return


    for i in range(start, n + 1): #start 시작인것이 포인트
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()

dfs(1)


N, M = map(int, input().split())
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N): #idx 시작인것이 포인트
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, i+1, N, M)
            visited[i] = False
            out.pop()
solve(0, 0, N, M)