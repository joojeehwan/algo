# bfs 풀이! 


from collections import deque



N = int(input())
MAP = []
maxNum = 0

for row in range(N):
    #한줄식 LIST에 담아서 구성!
    MAP.append(list(map(int, input().split())))
    #격자에서 가장 큰 점수도 구하기!
    for col in range(N):
        if MAP[row][col] > maxNum:
            maxNum = MAP[row][col]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def bfs(row, col, rain, visited):
    q = deque()
    q.append((row, col))
    visited[row][col] = True

    while q:
        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]
            if 0<= next_row < N and 0 <= next_col < N:
                if MAP[next_row][next_col] > rain and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))

ans = 0
#최고 수위까지 올리면서! 가장 많이 영역이 생기는 떄가 언제야?!
for i in range(maxNum):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    #BFS돌리면서 확인!
    for row in range(N):
        for col in range(N):
            if MAP[row][col] > i and not visited[row][col]:
                bfs(row, col, i, visited)
                cnt += 1

    if ans < cnt:
        ans = cnt

print(ans)


#dfs 풀이

'''
import sys 
sys.setrecursionlimit(10000) 
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 
def dfs(x, y, h): 

    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        
        if(0 <= nx < N) and (0 <= ny < N): 
            if arr[nx][ny] > h and done[nx][ny] == 0: 
                done[nx][ny] = 1 
                dfs(nx, ny, h) 
                
N = int(input()
arr = [list(map(int, input().split())) for _ in range(N)] 
ans = 0 


for k in range(max(map(max, arr))): # 주어진 배열에서 가장 큰값만큼 반복 

    # 매번 초기화 
    cnt = 0 
    done = [[0]*N for _ in range(N)]
     
     # 입력 받은 arr배열 탐색 
     for i in range(N): 
        for j in range(N): 
            if arr[i][j] > k and done[i][j] == 0: 
                done[i][j] = 1 
                cnt += 1 
                dfs(i, j, k) 
    ans = max(ans, cnt) 
    
print(ans)


'''