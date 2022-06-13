# '''
#
#
# 전형적인 bfs 문제
#
#
# '''
#
import sys

from collections import deque

input = sys.stdin.readline


n, m  = map(int, input().split())
#4줄 이니깐 행! 파이썬의 경우 열은 그냥 다 input이 받아 들이니깐!

#1. map 생성
MAP = [list(map(int, input().rstrip())) for _ in range(n) ]

# print(MAP)

#상 하 좌 우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

#2. 초기값 세팅 및 큐 생성

q = deque()
q.append((0,0))

while q:
    now_row, now_col = q.popleft()
    for i in range(4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]

        #장외가 아니면서, 통로인것!
        if 0 <= next_row < n and 0 <= next_col < m:

            if MAP[next_row][next_col] == 1 :

                #방문
                MAP[next_row][next_col] = MAP[now_row][now_col] + 1
                q.append((next_row, next_col))

print(MAP[n-1][m-1])
#
# import sys
# import collections
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# maze = [list(map(int, ' '.join(input()).split())) for _ in range(n)]
#
# # 이동
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# Q = collections.deque([(0, 0)])
# result = 0
#
# while Q:
#     x, y = Q.popleft()
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if maze[nx][ny] == 1:
#                 # 방문
#                 maze[nx][ny] = maze[x][y] + 1
#                 Q.append((nx, ny))
#
# print(maze[n - 1][m - 1])