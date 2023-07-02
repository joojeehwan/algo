'''



'''



def dfs(k, M):

    if k == M:
        for i in range(M):
            print(ans[i], end = " ")
        print("")
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            ans[k] = i
            dfs(k+1, M)
            visited[i] = 0 # 다른 곳에서 사용할 수 있게 넘겨줘야 한다


# 아 이걸 함수로 넘길 수가 없겟구나,,,!!

N, M = map(int, input().split())
ans = [0] * (M)
visited = [0] * (N + 1)

dfs(0,M)


############

#교수님 풀이

# N과 M(1)
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [-1] * N
check = [0] * (N + 1)
def dfs(k):
    # 이번에 k번째 수를 고르겠다.
    if k == M:
        for i in range(M):
            print(arr[i], end = " ")
        print("")
        return
    for i in range(1, N + 1):
        if check[i] == 1: continue # 이미 골랐던 수
        arr[k] = i
        check[i] = 1
        dfs(k + 1)
        check[i] = 0

dfs(0)