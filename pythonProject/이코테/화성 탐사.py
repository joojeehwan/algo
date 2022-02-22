'''

a -> b -> c 로 가는것과
a -> c 로 가는 것을 비교 한다는 마인드!


heapq를 사용해서! 풀어야 한다! => 거리 값이 가장 작은 것을 항상 빠르게 뽑아서 보내준다!

'''


import heapq
import sys

INF = int(1e9)

#
# distance = [INF] * (3) #1차원 배열
# n = 3
# distance2 = [[INF] * n for _ in range(n)] #2차원 배열?! => 문제에서 2차원 배열을 요구 하니깐,,! 그러네,,,!

# print(distance, distance2)

T = int(sys.stdin.readline())

#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):

    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]


    #최단거리 테이블 2차원 만들기

    distance = [[INF] * N for _ in range(N)]

    row, col = 0, 0
    #시작 노드로 가기 위한 비용은 (0, 0)위치의 값으로 설정하여, 큐에 삽입 => 0, 0도 값에 첨가 해야 하니깐!
    q = [(MAP[row][col], row, col)]
    distance[row][col] = MAP[row][col]
    
    #다익스트라 알고리즘 실행
    while q:

        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기!
        dist, row, col = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있다면 무시 => 무한대가 아니면 누가 이미 한번 건든 곳 이자나!?
        #이렇게 하면 visited배열을 안만들 수 있다
        if distance[row][col] < dist:
            continue
            
        #현재 노드와 연결된 다른 인접한 노드들을 확인

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            
            #맵의 범위를 벗어나는 경우 무시

            if next_row <  0 or next_row >= N or next_col < 0 or next_col >= N:
                continue

            #나를 거쳐서 가는 경우 dist : 현재 노드까지의 거리, MAP[next_row][next_col] 다음 번 노드를 포함하는 이동량
            cost = dist + MAP[next_row][next_col]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_row][next_col]:
                distance[next_row][next_col] = cost
                heapq.heappush(q, (cost, next_row, next_col))
            
    print(distance[N-1][N-1])
