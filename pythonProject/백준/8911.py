'''

구현

거북이

F : 한 눈금 앞으로
B : 한 눈금 뒤로 
L : 왼쪽으로 90도 회전
R : 오른쪽으로 90도 회전


거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이

처음에. (0, 0)에 있고 북쪽을 바라 봄.


1. 
걱북이가 지나간 영역을 어떻게 구하나 했는데...!
거북이가 지나간 영역(x, y) 에서 가장 큰 값과 가장 작은 값을 빼서 구하면 된다.


2. 
x축 y축을 기준으로 (0, 0)이 되기 때문에
보통에 내가 생각하는 이차원 배열로 벡터 배열을 구성하면 안돼

이렇게 수학적으로 주어진 건, 그냥 x, y로 풀자! 그게 안헷갈린다.
'''

#
# lst = [[1,4],[2,3],[3,2],[4,1]]
#
# print(max(lst, key=lambda x:x[0]))


n = int(input())

#북 서 남 동
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):

    pos_x = 0
    pos_y = 0
    pos_dir = 0
    move = list(input())
    trace = [(pos_x, pos_y)]

    for j in move:

        if j == "F":
            pos_x = pos_x + dx[pos_dir]
            pos_y = pos_y + dy[pos_dir]

        elif j == "B":
            pos_x = pos_x - dx[pos_dir]
            pos_y = pos_y - dy[pos_dir]

        # 모둘려 연산을 하는 것과 비교
        elif j == "L":
            if pos_dir == 3:
                pos_dir = 0
            else:
                pos_dir += 1

        elif j == "R":
            if pos_dir == 0:
                pos_dir = 3
            else:
                pos_dir -= 1
        trace.append((pos_x, pos_y))

    width = max(trace, key=lambda x:x[0])[0] - min(trace, key = lambda x:x[0])[0]
    height = max(trace, key=lambda x:x[1])[1]- min(trace, key = lambda x:x[1])[1]

    '''
      
    min_x = min(min_x, pos_x)
    min_y = min(min_y, pos_y)
    max_x = max(max_x, pos_x)
    max_y = max(max_y, pos_y)
    
    '''
    print(width * height)