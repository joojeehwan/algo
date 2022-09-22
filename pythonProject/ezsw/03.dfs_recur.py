



def dfs(node):

    visited[node] = True
    print(node, end = '')

    for next in range(n):
        #노드마다 하나씪 찎고, 반복 돌려서 다 확인
        if not visited[next] and MAP[node][next]:
            dfs(next)


n, e = map(int, input().split())
visited = [False for _ in range(n)]
MAP = [[0 for _ in range(n)] for _ in range(n)]

values = list(map(int, input().split()))
#노드의 갈 수 있음을 이차원 배열에 표시
for i in range(e):

    start, end = values[i * 2], values[i * 2 + 1]
    MAP[start][end] = MAP[end][start] = 1

dfs(0)
