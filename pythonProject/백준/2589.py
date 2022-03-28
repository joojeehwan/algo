'''

보물섬 bfs => 각 좌표마다 bfs를 돌리면 된다.

'''

from collections import deque

#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col):
    # 2. 큐 생성
    q = deque()
    #초기값 생성 및 checked 배열 만들기
    q.append([row, col])
    visited = [[False] * M for _ in range(N)]
    visited[row][col] = True
    num = 0 #최장의 이동거리를 담는,,!

    while q:
        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #범위 체크
            if 0 <= next_row < N and 0 <= next_col < M:
                #그리고 육지이면서 한번도 안들린 곳
                if MAP[next_row][next_col] == "L" and visited[next_row][next_col] == False:
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    num = max(num, visited[next_row][next_col]) #최단 거리이면서 가장 멀리 이동할 수 있는 최단 거리
                    q.append([next_row, next_col])
    return num - 1
N, M = map(int, input().split())

#1. 맵 생성
MAP = [list(map(str, input())) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == "L":
            cnt = max(cnt, bfs(i,j))

print(cnt)


