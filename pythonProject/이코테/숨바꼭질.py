import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


#노드의 개수, 간선의 개수를 입력받기

n, m = map(int, input().split())

#시작 노드를 1번 헛간으로 설정
start = 1
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]

distance = [INF] *(n + 1)


#모든 간선의 정보를 입력받기

for _ in range(m):
    frm, to = map(int, input().split())
    graph[frm].append((to, 1))
    graph[to].append((frm, 1))


def dijkstra(start):

    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #큐가 비어있지 않다면

        dist, now = heapq.heappop(q)

        #현재 노드가 이미 처리된 적이 있는 노드라면 무시

        if distance[now] < dist:
            continue
        
        # 현재 노드와 인접한 다른 노드 확인
        for next in graph[now]:
            next_now = next[0]
            next_dis = next[1]
            cost = dist + next_dis
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_now]:
                distance[next_now] = cost
                heapq.heappush(q, (cost, next_now))


dijkstra(start)

#최단 거리가 가장 먼 노드
max_node = 0

#도달할 수 있는 노드들 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
res = []

#반복문을 활용한 가장 큰것,,!
for i in range(1, n+ 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        res = [max_node]

    elif max_distance == distance[i]:
        res.append(i)

print(max_node, max_distance, len(res))


                
