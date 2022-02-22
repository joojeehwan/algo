graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}


from collections import deque


def bfs_iteration(graph, root):
    visited = []  ## visited = 방문한 노드들을 기록한 리스트
    queue = deque([root])  ## bfs는 queue개념을 이용한다.

    while (queue):  ## queue에 남은 것이 없을 때까지 반복
        node = queue.pop()  ## node : 현재 방문하고 있는 노드

        ## 현재 node를 방문한 적 없다. -> visited에 추가
        ## visited에 추가 후, 해당 노드의 자식 노드들을 queue에 추가
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])
    return visited


def dfs_iteration(graph, root):
    # visited = 방문한 꼭지점들을 기록한 리스트
    visited = []
    # dfs는 stack, bfs는 queue개념을 이용한다.
    stack = [root]

    while (stack):  # 스택에 남은것이 없을 때까지 반복
        node = stack.pop()  # node : 현재 방문하고 있는 꼭지점

        # 현재 node가 방문한 적 없다 -> visited에 추가한다.
        # 그리고 해당 node의 자식 node들을 stack에 추가한다.
        if (node not in visited):
            visited.append(node)
            stack.extend(graph[node])
    return visited


def dfs_recursive(graph, start, visited=[]):
    visited.append(start)  ## ★★★★★

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)  ## ★★★★★

    return visited

'''
visited = visited + [node]를 하게 되면
두 visited가 서로 다른 리스트를 참조하게 되므로
재귀 함수를 호출하면서 생기는 많은 함수들이
어떤 하나의 리스트에 모든 결과를 반영하는 것이 아니라
각자 독자적인 리스트를 갖게 되므로 저런 결과가 생기는 것.
각자 독자적인 리스트를 주면서, 앞의 visited.append(node)의 효과를 주고 싶다면
한가지만 더 수정해주면 될 것 같다.

for문 안에 (재귀)함수가 호출되는 부분이 있다.
dfs_recursive(graph, node, visited)를
visited = dfs_recursive(graph, node, visited)로 수정해주자.

'''


def dfs_recursive(graph, start, visited=[]):
    visited = visited + [start]  ## visited.append(start)대신 visited = visited + [start]를 대입
    print(visited)  # print(visited) 추가

    for node in graph[start]:
        if node not in visited:
            visited = dfs_recursive(graph, node, visited)  # 수정된 부분!

    return visited


paths = []


## 경로 탐색
def dfs_paths(graph, start, end, visited=[]):
    # 그 전에 방문했던 노드들을 기록하고
    # 이번 차례 방문하는 노드를 새로 추가한다.
    visited = visited + [start]

    # 도착할 경우, paths에 경로를 기록한다.
    if start == end:
        paths.append(visited)

    # 현재 노드의 자손 노드들 중, 방문하지 않은 노드들에 대해 재귀 호출
    for node in graph[start]:
        if node not in visited:
            dfs_paths(graph, node, end, visited)

dfs_paths(graph,'A','H')

## [['A', 'B', 'E', 'H'], ['A', 'C', 'F', 'H']]

