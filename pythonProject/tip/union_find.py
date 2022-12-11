# 두가지 모두 흐름은 알고 있어야 한다!

'''
최소 신장 트리

프림 알고리즘?


-남은 정점이 있으면,,
mst에 속한 정점 v, mst에 속하지 않고 가중치가 최소인 인접 w를 선택,,,


-최대한 적은 cost로 모든 맵을 밝히기

한 점을 탐색하면 그 점에서 갈 수 있는 모든 선에 대한 정보를 얻음


-한 그룹에서 갈 수 있는 선들 중 가장 코스트가 적은 선을 골라 그 선에 연결된
점을 해당 그룹에 포함함!


'''

# prim
"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

import heapq

n, m = map(int, input().split())
Graph = [[] for _ in range(n + 1)]
total_cost = 0
# 인접리스트
for i in range(m):
    f, t, cost = map(int, input().split())
    Graph[f].append((cost, t))
    Graph[t].append((cost, f))
# 1. 그래프 구성

hq = []
visited = [False] * (n + 1)  # 같은 그룹에 포함시켰는가?
# 2. 큐 선언 -> heap선언


# 3. 시작점(0번 점) 세팅 -> 시작점에 연결된 선 모두 heap에 추가
for cost, t in Graph[0]:
    heapq.heappush(hq, (cost, t))
visited[0] = True

while hq:
    # 4. now점 꺼내기 -> now 선 (가장 짧은 선)
    now = heapq.heappop(hq)
    now_cost = now[0]
    now_t = now[1]
    # 5. 이 선이 새로운 점을 연결하는 선인가? <- next찾기(판별)
    if visited[now_t]:
        continue
    total_cost += now_cost
    # 6. 새로운점 연결 <- next를 큐에 추가
    visited[now_t] = True
    for cost, t in Graph[now_t]:
        heapq.heappush(hq, (cost, t))
print(total_cost)

'''

쿠르스컬 알고리즘 => 같은 그룹이 아닌 녀석들만 연결하자! 

가중치 순으로 정렬! (오름차순) 필수!
가중치가 낮은 녀석부터 선택

but 사이클이 생기지 않도록!

파인드셋 해서 부모가 다르면! 사이클이 생기지 않는 것!
그리고 유니온까지 사용해서! 계속 대표원소를 갱신한다!


'''

# 선에 초점
"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""


def Find(x):
    if x == parents[x]:
        return x
    else:
        px = Find(parents[x])
        parents[x] = px
        return px


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
edges = []
for i in range(m):
    # 비교의 기준이 되는 cost를 먼저 넣는다.
    f, t, cost = map(int, input().split())
    edges.append((cost, f, t))
edges.sort()
total_cost = 0
for cost, f, t in edges:
    # 이미 같은 그룹이었다면 무시
    # 같은 그룹끼리의 연산이 되지 않도록 방지
    if Find(f) == Find(t):
        continue
    Union(f, t)
    total_cost += cost

print(total_cost)
# 유튜브 수업때 설명한 코드들은 '모든 node가 전부 연결 가능하다.'



# 주지환 velog 정리
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출

    if parent[x] == x:
        return x

    px = find_parent(parent, parent[x])
    parent[x] = px

    return px


def union(x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    # 더 작은 수의 값을 조상으로,,!
    if a < b:
        parent[b] = a

    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [i for i in range(v + 1)]

edges = []
result = 0

# 단반향
for _ in range(e):
    frm, to, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정

    edges.append((cost, frm, to))

edges.sort()

for edge in edges:
    cost, a, b = edge  # 오 이렇게 가능!

    # 사이클이 발생하지 않을 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union(a, b)
        result += cost

print(result)



