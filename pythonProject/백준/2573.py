''''


빙산
지구 온난화로 인하여 북극의 빙산이 녹고 있다. 빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자. 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당되는 칸에는 0이 저장된다. 그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.


 	2	4	5	3
 	3	 	2	5	2
 	7	6	2	4

그림 1. 행의 개수가 5이고 열의 개수가 7인 2차원 배열에 저장된 빙산의 높이 정보

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 따라서 그림 1의 빙산은 일년후에 그림 2와 같이 변형된다.

그림 3은 그림 1의 빙산이 2년 후에 변한 모습을 보여준다. 2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다. 따라서 그림 2의 빙산은 한 덩어리이지만, 그림 3의 빙산은 세 덩어리로 분리되어 있다.


 	 	2	4	1
 	1	 	1	5
 	5	4	1	2

그림 2


 	 	 	3
 	 	 	 	4
 	3	2

그림 3

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

예제 입력1

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0


2

'''
#bfs로 풀이

import sys
from collections import deque
input = sys.stdin.readline

#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#덩이리씪 파악하기 좋으니깐! bfs로 한다!
def bfs():

    #빙산있는 곳만 인덱스로 따로 뽑아서 진행
    q = deque()
    q.append(artic[0])
    visied = [[False] * m for _ in range(n)]
    visied[artic[0][0]][artic[0][1]] = True

    select_iceberg = 0 #탐색한 빙산
    reduce = []

    #녹일 빙산 탐색
    while q:
        now_row, now_col  = q.popleft()

        select_iceberg += 1
        cnt = 0 #인접한 바다 갯수 => 0의 갯수

        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]
            # 항상 범위 생각
            if 0 <= next_row < n and 0 <= next_col < m:
                #주위에 바다가 있으면
                if MAP[next_row][next_col] == 0:
                    # 그 수만큼 cnt를 증가
                    cnt += 1
                elif MAP[next_row][next_col] > 0 and not visied[next_row][next_col] : # 빙산인데, 안가본 곳
                    visied[next_row][next_col] = True
                    q.append((next_row, next_col))

        if cnt != 0:
            reduce.append((now_row, now_col, cnt))

    #녹이기
    for row, col , height in reduce:
        #0 이하로는 녹여지지 않는다.
        if MAP[row][col] - height > 0 :
            MAP[row][col] = MAP[row][col] - height
        else:
            MAP[row][col] = 0
        # 다 녹인 다음에 그 다음의 bfs를 위해서 artic에서 삭제!
        if MAP[row][col] == 0 and (row, col) in artic:
            #인덱스가 아니라 값을 직접 삭제
            artic.remove((row, col))

    return select_iceberg
n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

answer = 0
artic = [] #빙산


for i in range(n):
    for j in range(m):
        #빙산 찾기
        if MAP[i][j] != 0:
            artic.append((i, j))

while True:
    # 덩어리가 2개 이상인 경우!
    if len(artic) != bfs():
        break

    answer += 1

    if sum(map(sum, MAP[1:-1])) == 0: #빙하가 다 녹을떄 까지 덩어리가 2개 이상이 안된다.
        answer = 0
        break

print(answer)



#python 문법 정리,,
# arr = [[1,2,3], [4,5,6],[7,8,9], [10, 11,12]]

# #처음과 양쪽 끝 삭제
# print(arr[1:-1])
# print(list(map(sum, arr[1:-1])))

'''
map(function, iterable)

map 함수의 모양은 위와 같습니다.
첫 번째 매개변수로는 함수가 오고
두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)이 옵니다.

map(적용시킬 함수, 적용할 값들)

arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라는 말입니다.
만약 A가 None 이라면, 처음부터 라는 뜻이고
B가 None 이라면, 할 수 있는 데까지 (C가 양수라면 마지막 index까지, C가 음수라면 첫 index까지가 되겠습니다.)라는 뜻입니다.
마지막으로 C가 None 이라면 한 칸 간격으로 라는 뜻입니다.


'''

# dfs 풀이

import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

def melt(x, y):
    cnt = 0  # 인접한 바다 개수

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                cnt += 1

    if cnt != 0:
        return x, y, cnt
    else:
        return None

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and arr[nx][ny] != 0:
                dfs(nx, ny)

# 입력
N, M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(N)]

# 풀이
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

while True:
    answer += 1

    # 1. 빙하 녹이기
    reduce = []  # x, y, 녹는 높이
    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0:
                h = melt(x, y)

                if h is not None:
                    reduce.append(h)

    for x, y, h in reduce:
        arr[x][y] = arr[x][y] - h if arr[x][y] - h > 0 else 0

    # 2. 빙하 개수 구하기
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0 and not visited[x][y]:
                cnt += 1

                if cnt == 2:
                    break

                dfs(x, y)

    if cnt > 1:  # 종료 조건
        break

    if sum(map(sum, arr[1:-1])) == 0:  # 빙하가 다 녹을때까지 덩어리가 1개?
        answer = 0
        break

# 출력
print(answer)