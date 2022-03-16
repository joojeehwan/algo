
'''
DFS와 BFS

'''

import sys
from collections import deque



def dfs(node):
    print(node, end = " ")
    visited[node] = True
    for i in MAP[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    visited[node] = True
    q = deque([node])
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in MAP[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
N, M, V = map(int, input().split())


MAP = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    start, end = map(int, input().split())
    MAP[start].append(end)
    MAP[end].append(start)

for i in range(1, N + 1):
    MAP[i].sort()

dfs(V)

visited = visited = [False] * (N + 1)
print()
bfs(V)


