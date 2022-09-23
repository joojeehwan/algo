from collections import deque


def bfs(node):

    visited = [False for _ in range(n)]
    q = deque()
    visited[node] = True
    q.append((node))

    while q:

        now_node = q.pop()
        print(now_node, end = ' ')

        for next in range(n):
            if not visited[next] and MAP[now_node][next]:
                visited[next] =  True
                q.append((next))



n, e = map(int, input().split())
MAP = [[0 for _ in range(n)] for _ in range(n)]
values = list(map(int, input().split()))

#노드의 갈 수 있음을 이차원 배열에 표시
for i in range(e):

    start, end = values[i * 2], values[i * 2 + 1]
    MAP[start][end] = MAP[end][start] = 1

bfs(0)
