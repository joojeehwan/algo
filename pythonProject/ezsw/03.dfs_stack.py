'''

입력

5 6
0 1 0 2 1 3 1 4 2 4 3 4

'''


def dfs(node):
    visited = [False for _ in range(n)]
    stack = []
    stack.append(node)
    while stack:
        curent = stack.pop()
        if visited[curent]:
            continue

        visited[curent] = True
        print(curent, end = ' ')
        for next in range(n):
            if not visited and MAP[curent][next]:
                stack.append(next)

n, e = map(int, input().split())
visited = [False for _ in range(n)]
MAP = [[0 for _ in range(n)] for _ in range(n)]

values = list(map(int, input().split()))
#노드의 갈 수 있음을 이차원 배열에 표시
for i in range(e):

    start, end = values[i * 2], values[i * 2 + 1]
    MAP[start][end] = MAP[end][start] = 1

dfs(0)
