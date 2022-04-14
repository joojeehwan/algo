import sys

sys.stdin = open("sample_input.txt", "r")

# 상 하 좌 우 좌상 우상
dr = [-1, 1, 0, 0, -1, -1]
dc = [0, 0, -1, 1, -1, 1]

T = int(input())

def dfs(row, col, cnt, SUM):
    global ans

    if cnt == 4:
        ans = max(ans, SUM * SUM)
        # print(lst)
        return
    de = 1
    for i in range(6):

        next_row = row + dr[i]
        next_col = col + dc[i]

        if 0 <= next_row < M and 0 <= next_col < N :
            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                dfs(next_row, next_col, cnt + 1, SUM + MAP[next_row][next_col])
                visited[next_row][next_col] = False


for tc in range(1, T + 1):

    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    ans = 0
    for i in range(M):
        for j in range(N):
            visited[i][j] = True
            dfs(i, j, 1, MAP[i][j])
            # visited[i][j] = False
    print("#%d" %tc, end =" ")
    print(ans)
