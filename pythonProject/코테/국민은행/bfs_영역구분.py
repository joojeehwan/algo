'''

10026 적색록약  // 현대 IT&E 기출 확인


어제 물론 좌표에 푸는 문제라, 당황했다고는 하지만, 나중에 차선으로 생각한 방향으로 풀때도, 익숙하지 않아서 실수 했다.


영역을 세는 방법의 수는 2가지(현재 내가 아는)

1. global로 cnt를 만들고 bfs의 while문 안이 아니라 바깥에서 cnt를 증가. (현대 it&E)


2. 아래와 같은 코드를 줘서, 같은 곳으로만 이동하게 하고, bfs가 끝날 떄마다 cnt를 증가 시키는 형태

  <bfs 중 일부 발췌>
  if MAP[next_row][next_col] == MAP[start_row][start_col]:
                q.append([next_row, next_col])
                visited[next_row][next_col] = 1


  cnt = 0
  for row in range(N):
    for col in range(N):
      if visited[row][col] == 0:
        bfs(row, col)
        cnt += 1

'''

'''


적록색약


이게 왜 bfs이지,,?!

그걸 알아야 한다,, bfs인 이유를 알아야 해!

2차원 배열의 넓이에 대한 문제,,?! bfs/dfs를 생각 해야대!

적록색약용 배열 하나 만들고
일반욕 배열 하나 만들어서
bfs돌고! bfs탐색이 끝날 떄마다(같은 색깔의 칸들을 탐색이 끝날떄마다) cnt를 하나 씩 증가!


'''

from collections import deque


def bfs(start_row, start_col):
    # 상 하 좌 우
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q.append([start_row, start_col])
    visited[start_row][start_col] = 1

    while q:
        now = q.popleft()
        now_row = now[0]
        now_col = now[1]
        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue

            if visited[next_row][next_col] != 0:
                continue

            if MAP[next_row][next_col] == MAP[start_row][start_col]:
                q.append([next_row, next_col])
                visited[next_row][next_col] = 1

                # 처음에 들어오는 값들을 검색해야 하니깐! 같은색,,,!


N = int(input())
q = deque()
MAP = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 일반 먼저 확인
cnt = 0
for row in range(N):
    for col in range(N):
        if visited[row][col] == 0:
            bfs(row, col)
            cnt += 1

print(cnt, end=" ")

# 그 다음에 적록색약 확인
for row in range(N):
    for col in range(N):
        if MAP[row][col] == "R":
            MAP[row][col] = "G"

visited = [[0] * N for _ in range(N)]

cnt = 0
for row in range(N):
    for col in range(N):
        if visited[row][col] == 0:
            bfs(row, col)
            cnt += 1
print(cnt)



#현대 IT&E

#BFS를 통해서 무리 나누기!


from collections import deque

answer = 0

def bfs(start_node, new_data, visited):
    global answer

    if visited[start_node] == True:
        return

    #초기값 설정
    q = deque()
    q.append((start_node))
    visited[start_node] = True
    while q:
        now_point = q.popleft()
        for next_point in new_data[now_point]:
            if not visited[next_point]:
                q.append((next_point))
                visited[next_point] = True
    answer += 1

def solution(V, bridge):
    # 데이터 전처리
    new_data = [[] for _ in range(V + 1)]
    for i in range(len(bridge)):
        new_data[bridge[i][0]].append(bridge[i][1])

    #방문 check 배열 만들기
    visited = [False] * (V + 1)

    #bfs 실행
    for node in range(1, V+1):
        bfs(node, new_data, visited)
    return answer - 1

#수정해야할 내 풀이

from collections import deque


#델타 배열 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def bfs(start_row, start_col, m, n, MAP):

    q = deque()
    q.append((start_row,start_col))
    #visited = [[False] * (m + 1) for _ in range(n + 1)]
    visited[start_row][start_col] = True
    global answer

    if MAP[start_row][start_col] == -1:
        return

    while q :
        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if  0 <= next_row < n and 0 <= next_col < n :
                if not visited[next_row][next_col] and MAP[next_row][next_col] == 0:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))


def solution(n, m, points):

    MAP = [[0] * (m + 1) for _ in range(n + 1)]
    for point in points:
        row, col = point
        MAP[row][col] = -1
    answer = 0
    visited = [[False] * (m + 1) for _ in range(n + 1)]

    for row in range(m):
        for col in range(n):
            if not visited[row][col]:
                bfs(row, col, m, n, MAP)


    return answer














