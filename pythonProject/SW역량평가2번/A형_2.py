# import sys
#
from collections import deque
#
# sys.stdin = open("sample_input.txt", "r")

#bfs로 해보자

#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(row, col):

    q = deque()
    q.append((row, col))

    visited[row][col] = 1
    while q:

        now_row, now_col = q.popleft()

        # if MAP[now_col][now_col] != 0:

        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #범위 밖에 아웃
            if next_row <= 0 or next_row > N or next_col <= 0 or next_col >= N:
                continue

            if visited[next_row][next_col] != 0:
                continue

            #몬스터나 고객이 있다면
            if MAP[next_row][next_col] != 0 :
                q.append(([next_row, next_col]))
                visited[next_row][next_col] = visited[now_row][now_col] + 1


N = int(input())
#MAP 구성
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

de = 1

bfs(1, 1)

print(visited)





