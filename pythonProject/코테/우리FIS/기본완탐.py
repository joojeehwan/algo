'''




4 2
1 0 0 1
0 0 0 2
0 2 0 1
0 0 0 2

'''




N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0 , -1, 1]


for row in range(N):
    for col in range(N):

        if MAP[row][col] == 1:
            
            # M 범위안에 있는지 확인
            flag = False
            for power in range(1, M):
                # 4방향 이동
                for dir in range(4):
                    next_row = row + dr[dir] * power
                    next_col = col + dc[dir] * power
                    
                    #범위 안에 있고
                    if 0 <= next_row < N and 0 <= next_col < N:
                        #범위 안에 2가 없으면, 1이 사라진다.
                        if MAP[next_row][next_col] == 2:
                            flag = True

            #끝까지 2를 찾지 못함.
            if not flag:
                MAP[row][col] = 0

            else:
                MAP[row][col] = 1

ans = 0

for row in range(N):
    for col in range(N):
        if MAP[row][col] == 1:
            ans += 1

print(ans)

