# dfs flood fill

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(row, col, color):

    visited = [[False for _ in range(n)] for _ in range(n)]
    stack = []
    stack.append((row, col))

    while stack :
        row, col = stack.pop()
        if visited[row][col]:
            continue

        visited[row][col] = True
        MAP[row][col] = color

        for i in range(4):

            next_row = row + dr[i]
            next_col = col + dc[i]
            if next_row < 0 or next_row > n -1 or next_col < 0 or next_col > n -1 :
                continue
            if visited[next_row][next_col]:
                continue
            stack.append((next_row, next_col))

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

sr, sc, color = map(int, input().split())
dfs(sr, sc, color)

for i in range(n):
    for j in range(n):
        print(MAP[i][j], end =' ')
    print()