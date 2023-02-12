'''
1. 출발 노드를 설정한다

2. 최단거리 테이블을 초기화한다.

-> 다른 모든 노드로 가는 최단거리를 '무한'으로 초기화한다

3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다.

-> 이때 선택된 노드의 최단거리는 확정된다.

4. 해당 노드를 거쳐 다른 노드로 가는 비용를 게산하여 최단 거리 테이블을 갱신한다.

5. 3~4 과정을 반복한다.



2022 11.24 공부
'''


#힙큐 쓴 풀이

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


#노드의 갯수, 간선의 갯수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
#최단거리 테이블
distance = [INF]*(n + 1)

#노드 연결정보
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    #frm번 노드에서 to번 노드로 가는 비용 cost
    frm, to, c = map(int, input().split())
    graph[frm].append((to, c))
    
#다익스트라 알고리즘!최소힙 사용! => 최단거리 테이블에서 거리 갱신 이후에 가장 작은 값을 뽑는,,!
# 이것이 바로 자료구조를 사용하는 이유

def dijkstra(start):
    q = []
    #시작 노드 설정
    heapq.heappush(q, (0, start))
    # 시작은 당연히 거기까지 거리가 0이지!
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) #최소힙에서 꺼내! 가장 최단거리 테이블 작은애!

        #기존에 있는 거리보다 긴 곳이라면! 쳐다볼 필요도 없음.
        #그냥 원래 있던 길로 가면 되니!
        if distance[now] < dist:
            continue

        #선택된 노드의 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] #해당 노드를 거쳐 갈 때 거리
            #선택된 노드를 거쳐서 가는것이 현재 가는 거리보다 작다면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우
  if distance[i] == INF:
    print("infinity")
  else:
    print(distance[i])

            
            

#힙큐 안쓴 풀이

n, m = map(int, input().split())
k = int(input())  # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n + 1)]  # 1번 노드부터 시작하므로 하나더 추가

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())  # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치
    graph[u].append((v, w))  # 거리 정보와 도착노드를 같이 입력합니다.


def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0  # 시작 노드는 0으로 초기화
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]  # 시작 노드와 연결된 노도들의 거리 입력

    for _ in range(n - 1):
        now = get_smallest_node()  # 거리가 구해진 노드 중 가장 짧은 거리인 것을 선택
        visited[now] = True  # 방문 처리

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:  # 기존에 입력된 값보다 더 작은 거리가 나온다면,
                distance[j[0]] = distance[now] + j[1]  # 값을 갱신한다.


dijkstra(k)
print(distance)

# 5 6
# 1
# 5 1 1
# 1 2 1
# 1 3 3
# 2 3 1
# 2 4 5
# 3 4 2
# 예시를 입력하면 아래와 같이 나온다. 0번 인덱스는 편의상 만든 것이기에 무시하면 되고, 예상했던대로 0 1 2 4 INF 가 나오는것을 확인할 수 있다.
# [100000000.0, 0, 1, 2, 4, 100000000.0]


#변수명 이렇게 설정하자

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())

MAP = [[] for _ in range(N + 1)]

# 초기 값 세팅
for _ in range(M):
    # 무방향 그래프 가정
    frm, to, value = map(int, input().split())
    MAP[frm].append((to, value))
    MAP[to].append((frm, value))

# 1번 노드에서 부터 시작한다고 가정

distance = [INF] * (N + 1)


def dijkstra(start):
    q = []
    heapq.heapqpush(q, (0, start))
    distance[start] = 0
    while q:

        value, now_node = heapq.heappop(q)

        if distance[now_node] < value:
            continue

        for next_node, next_value in MAP[now_node]:

            cost = value + next_value

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heapqpush(q, (cost, next_node))

    return distance
