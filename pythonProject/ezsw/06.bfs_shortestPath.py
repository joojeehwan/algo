'''

입력

5
0 0 0 0 0
0 1 1 1 1
0 0 0 0 0
1 1 1 1 0
0 0 0 0 0
0 1 4 2

'''


# bfs 최단거리
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(s_row, s_col, d_row, d_col):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((s_row, s_col, 0))
    visited[s_row][s_col] = True

    while q:
        now_row, now_col, dis = q.popleft()
        
        #도착지에 도착
        if now_row == d_row and now_col == d_col :
            return dis

        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if 0 <= next_row < n and 0 <= next_col < n:
                if not visited[next_row][next_col] and MAP[next_row][next_col] == 0:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col, dis + 1 ))
    return -1

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

sr, sc, dr, dc = map(int, input().split())
print(bfs(sr, sc, dr, dc))

