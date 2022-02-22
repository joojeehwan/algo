'''

아기 상어

방법이 2가지가 있음,, bfs인건 맞구먼! 그냥 정렬을 하는 방법이 있고, heap자료구조를 이용하는 방법이 있음,, 그냥 정렬의 방법을 사용하는게 좋을 거 같다.
'''


# from collections import deque
#
# #입력
# n = int(input())
#
# MAP = [list(map(int, input().split())) for _ in range(n)]
#
# #델타 배열
# #상 하 좌 우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # 초기 값 설정
# now_row , now_col = 0, 0
#
# #상어 위치 판단
# for row in range(n):
#     for col in range(n):
#         if MAP[row][col] == 9:
#             #상어가 있는 곳은 다음에 갈 수 있으니
#             MAP[row][col] = 0
#             now_row = row
#             now_col = col
#             break
# size = 2 #상어 크기
# eat = 0 #상어가 먹은 먹이의 수
# move_count = 0 #상어의 이동거리
#
# #bfs 시작
#
# #먹이가 없을때까지 무한 반복해야 하니! bfs한번하고 끝내는게 아니라! 계속 먹이를 먹어야 하니깐!
# while True:
#     # 큐 생성
#     q = deque()
#     # 시작점 세팅(시작점을 queue에 추가)
#     q.append((now_row, now_col, 0))
#     #
#     visited = [[False] * n for _ in range(n)]
#     flag = 1e9
#     fish = []
#     while q:
#         #맨 앞점을 꺼내기
#         start_row, start_col, count = q.popleft()
#
#         #최소 이동시간보다 많은 곳은 굳이 탐색하지 않는다. => 최단거리
#         if count > flag:
#             break
#         #4방향 탐색
#         for i in range(4):
#             next_row = start_row + dr[i]
#             next_col = start_col + dc[i]
#
#             #이제 판단 => 공간안에 있고, 가본적이 없는 곳이고, 아기 상어의 크기보다 작은 물고기
#
#             #1. 장외 판단 => 장외면 못가고!
#             if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
#                 continue
#
#             #2. 한번도 가보지 않은곳이면 못가고, 아기 상어보다 값이 큰곳이라면 못가고
#             if MAP[next_row][next_col] > size or visited[next_row][next_col]:
#                 continue
#
#             #이제 물고기 있는 곳 판단! 빈칸하고 구별 => 먹을 수 있는 물고기를 담음
#             if MAP[next_row][next_col] != 0 and MAP[next_row][next_col] < size:
#                 fish.append((next_row, next_col, count + 1))
#                 #flag를 둠으로써 굳이 최단거리가 아닌 물고기들을 탐색x => 시간초과 예방
#                 flag = count
#             visited[next_row][next_col] = True
#             q.append((next_row, next_col, count + 1))
#
#     #담을 수 있는 물고기들을 다 담고, 조건에 맞게 물고기를 식사(위에서 왼쪽)
#     if len(fish) > 0:
#         fish.sort()
#         #가장 맨앞에 있는 것! 이차원배열에서!
#         row, col, move = fish[0][0], fish[0][1], fish[0][2]
#         #그때 그 물고기를 먹을때의 이동거리를 위에서 구했으니 먹을때 더해준다.
#         move_count += move
#         eat += 1
#         #이제 식사했으니 그곳은 없는 곳!
#         MAP[row][col] = 0
#         #내 몸만큼 먹었으면 사이즈 up
#         if eat == size:
#             size += 1
#             eat = 0
#         #시작위치 change
#         now_row = row
#         now_col = col
#     else:
#         break
#
# print(move_count)


#sol 2

from collections import deque
import heapq


#bfs탐색
def bfs(row, col):
    global size, move_count, eat
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    #아기 상어가 먹을 수 있는 물고기 없을때 까지 반복
    while True:
        queue = deque((row, col, 0)) #아기 상어의 row, col, 이동시간
        visited = [[False] * n for _ in range(n)]
        visited[row][col] = True #현재 아기 상어의 위치
        heap = [] #아기 상어가 먹을 수 있는 물고기
        flag = 1e9 #아기 상어의 최소 이동시간

        #아기 상어가 갈 수 있는 모든 곳을 탐색
        while queue:
            a, b, count = queue.popleft()

            #아기 상어의 최소 이동시간보다 많은 시간이 필요한 곳부터는 탐색을 하지 않는다.
            if count > flag:
                continue
            #델타 배열 탐색
            for i in range(4):
                next_row = a + dr[i]
                next_col = b + dc[i]
                
                #공간안에 있고, 탐색하지 않았고, 아기 상어의 크기보다 작거나 같은 물고기 이거나 빈공간이라면
                if 0<= next_row < n and 0<next_col<n and visited[next_row][next_col] == False and MAP[next_row][next_col] <= size:
                    #아기 상어보다 작은 물고기 이고 공간이 아니라면
                    if MAP[next_row][next_col] < size and MAP[next_row][next_col] != 0:
                        heapq.heappush(heap, (next_row, next_col, count + 1)) #먹을 수 있는 물고기를 힙에 추가
                        flag = count # 아기 상어의 최소 이동시간을 초기화
                        
                    queue.append((next_row, next_col, count + 1))
                    visited[next_row][next_col] = True
                    
        #아기 상어가 먹을 수 있는 물고기가 있다면
        if len(heap) > 0 :
            # 위, 왼쪽에서의 물고기 부터 우선적으로 먹으야 하므로! heapq를 사용
            x, y, move = heapq.heappop(heap)
            move_count += move
            eat += 1
            MAP[x][y] = 0

            if eat == size:
                size += 1
                eat = 0

        else:
            break



n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
size = 2
move_count = 0
eat = 0

#아기 상어의 위치를 찾는다
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 9:
            MAP[i][j] = 0 #아기 상어의 위치를 0으로 초기화
            bfs(i, j)  #bfs탐색 시작
            break
print(move_count)

'''

import sys
from collections import deque
import heapq


# bfs 탐색
def bfs(x, y):
    global res, eat, size
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 아기 상어가 먹을 수 있는 물고기가 없을 때까지 반복
    while True:
        queue = deque([[x, y, 0]]) # 아기 상어의 x좌표, y좌표, 이동 시간
        visited = [[False] * n for _ in range(n)] # 탐색 여부
        visited[x][y] = True # 현재 아기 상어의 위치
        heap = [] # 아기 상어가 먹을 수 있는 물고기
        flag = n ** 2 # 아기 상어의 최소 이동 시간

        # 아기 상어가 갈 수 있는 모든 곳을 탐색
        while queue:
            a, b, cnt = queue.popleft()

            # 아기 상어의 최소 이동 시간보다 많은 시간이 필요한 곳부터는 탐색을 멈춘다.
            if cnt > flag:
                break

            # 상/하/좌/우 탐색
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                # 공간 안에 있고 탐색하지 않았고 아기 상어의 크기보다 작거나 같은 물고기 이거나 공간이라면
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] <= size:
                    # 아기 상어보다 작은 물고기 이고 공간이 아니라면
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        heapq.heappush(heap, (nx, ny, cnt + 1)) # 먹을 수 있는 물고기를 힙에 추가
                        flag = cnt # 아기 상어의 최소 이동시간을 초기화

                    queue.append([nx, ny, cnt + 1])
                    visited[nx][ny] = True

        # 아기 상어가 먹을 수 있는 물고기가 있다면
        if len(heap) > 0:
            # 위, 왼쪽에 물고기 부터 우선적으로 먹어야 하기때문에 heapq 를 사용
            x, y, move = heapq.heappop(heap)
            res += move # 이동 시간을 더해준다.
            eat += 1 # 물고기를 먹는다.
            graph[x][y] = 0 # 먹은 물고기의 자리는 0으로 초기화

            # 먹은 물고기의 수가 아기 상어의 크기와 같다면
            # 아기 상어의 크기를 올려준다.
            if eat == size:
                size += 1
                eat = 0

        # 먹을 물고기가 없으면 탐색을 멈춰준다.
        else:
            break


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
size = 2 # 아기 상어의 크기
res = 0 # 최소 이동 시간
eat = 0 # 먹은 물고기 수

# 아기 상어의 위치를 찾는다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0 # 아기 상어의 위치를 0으로 초기화
            bfs(i, j)
            break
print(res)

'''