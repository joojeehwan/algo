'''

구현 + 시물레이션 문제

삼성기출문제

포인트!
- 방향이 d일 떄, 왼쪽으로 회전한 뒤 방향은 (d + 3) % 4(북 : 0, 동 : 1, 남 : 2, 서 : 3)
- 인접한 4방향을 모두 탐색하면서 로봇청소기가 이동가능한 방향(벽 x, 이미 청소한곳x)이면 바로 이동하고 탐색 멈춤


말 그대로 그냥 빡구현!

'''

#북 동 남 서  =>문제에 주어진 대로 구현해야함
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]



#뒤로 후진하는 함수

def getBack(row, col, dir):
    if dir == 0 or dir == 1:
        next_row = row + dr[dir+2]
        next_col = col + dc[dir+2]

    if dir == 2 or dir == 3 :
        next_row = row + dr[dir-2]
        next_col = col + dc[dir-2]

    return next_row, next_col



#기본적인 입력받기
n, m = map(int, input().split())

row, col, dir = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

#청소 여부를 확인!
visited = [[False] * m for _ in range(n)]
visited[row][col] = True
count = 1 #로봇 청소기가 청소하는 칸의 갯수

while True:
    flag = False #4방향 다 돌아도 청소할곳을 못찾을때 후진할떄 사용할 flag값

    for _ in range(4):
        #현재 바라보고 있는 방향 기준으로 왼쪽으로 방향 전환이니깐!
        next_row = row + dr[(3+dir) % 4]
        next_col = col + dc[(3+dir) % 4]

        #범위 체크 => 청소가 가능한 지역 (범위 안, 벽x, 이전에 청소 안한 곳)

        if 0<= next_row < n and 0 <= next_col < m and visited[next_row][next_col] == False and MAP[next_row][next_col] == 0:
            dir = (3+dir) % 4 # 갔으니 다시 방향을 바꾼다. =>그 다음 이동을 위해서
            visited[next_row][next_col] = True
            #직접 이동!
            row = next_row
            col = next_col
            #청소한 곳이 있으니 count증가
            count += 1
            flag = True
            break #아 브레이크 있고 다시 처음부터 방향기준으로 탐색해야한다
        else:
            #그냥 방향만 바꾼다
            dir = (3 + dir) % 4  # 갔으니 다시 방향을 바꾼다.

    #4방향 다 돌고도! flag값이 그대로 fale면! 후진!
    if flag == False:
        back_row, back_col = getBack(row, col, dir)
        if MAP[back_row][back_col] == 1 :#벽이면
            break
        else:
            #벽이 아니면 후진해서 그 칸으로 가자!
            row = back_row
            col = back_col
            # row, col = back_row, back_col

print(count)

