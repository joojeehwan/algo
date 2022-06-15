'''

2가지 방법으로 한번 풀어보자!


이중 포문으로 MAP전체를 돌면서 1이면 dfs들어간다!
그래서 0으로바꾸면서 count 세면,,! 이런 아이디어!

'''


#dfs 풀어보기! 

#기본적인 입력받기
n = int(input())
MAP = [list(map(int, input())) for _ in range(n)]

#정답이 담길 리스트
num = []

#델타 배열 만들기
#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(row, col):

    global count
    #범위 체크 / 1인곳만 간다!
    if 0<= row < n and 0<= col < n:
        if MAP[row][col] == 1:
            count += 1
            MAP[row][col] = 0

            #사방향으로 dfs가 갈 수 있으니!
            for i in range(4):
                next_row = row + dr[i]
                next_col = col + dc[i]
                dfs(next_row, next_col)
            return True
        return False

#개별 단지의 갯수를 세는
count = 0

#몇개의 단지가 존재하는지
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(count)
            result += 1
            #다시 숫자가 몇개인지 카운트 해야 하니깐 센다
            count = 0


num.sort()
print(result)
for i in range(len(num)):
    print(num[i])





#bfs로 풀어보기
'''

bfs로 구역을 자를떄까지 다 돈다는 늒미!


'''
from collections import deque

n = int(input())

MAP = [list(map(int, input())) for _ in range(n)]



#델타 배열 만들기
#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(MAP ,row, col):
    #2. 큐 생성
    q = deque()
    q.append((row, col))
    MAP[row][col] = 0 #탐색중인 위치 0으로 바꾸어서 다시 안가도록!
    cnt = 1

    #큐 돌리기 시작!
    while q:
        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if 0<= next_row < n and 0<= next_col < n:

                if MAP[next_row][next_col] == 1:
                    MAP[next_row][next_col] = 0
                    q.append((next_row, next_col))
                    cnt += 1
    return cnt

n = int(input())

#1. 초기 맵 구성
MAP = [list(map(int, input())) for _ in range(n)]

#여기서 차이가 난다! => dfs와의 차이
cnt = []
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1:
            #각각의 개수를 그냥 bfs돌고 그 결과를 cnt에다 담아서!
            cnt.append(bfs(MAP, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])



#dfs visited배열 + dfs

n = int(input())

MAP = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

#델타 배열 만들기
#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    global  cnt
    visited[row][col] = True
    if MAP[row][col] == 1:
        cnt += 1

    for i in rang(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0<= nr < n and 0 <= nc < n:
            if visited[nr][nc] == False and MAP[nr][nc] == 1:
                dfs(nr, nc)



cnt = 0
housing = []
# 정의된 dfs를 가지고 graph를 탐색

for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            housing.append(cnt)
            cnt = 0

# 문제 답 도출
housing.sort()  # 오름차순 정렬
print(len(housing))
for i in housing:
    print(i)
