from collections import deque


def bfs(graph, start, end):
    visited = [False] * len(graph)
    q = deque()
    q.append(start)
    visited[start] = True
    # 이전 노드를 기록하는 배열
    prev = [-1] * len(graph)

    while q:
        now_node = q.popleft()
        debug = 1
        for next_node in graph[now_node]:
            if not visited[next_node]:
                q.append(next_node)
                # 다음 번 갈 노드와 현재 내가 있는 노드를 알 수 있으니,
                # "다음 번 갈 노드(next_node)의 이전은 무엇?! 그건 바로 지금(now_node)"
                # prev라는 배열안에는, start 부터 end까지 가면서, 어떤 노드를 통해 이동했는지 기록
                # ex) [-1, 0, 0, 1, 1, 2, 2]
                # 라고 적혀있다면, start 0번 노드 , end 6번노드 이므로,
                # 6번 노드에 최단거리로 도착하기 위해 2번노드 방문 => prev[6] = 2
                # 2번 노드에 최단거리로 도착하기 위해 0번노드 반문 => prev[2] = 0
                # 0번 노드는 시작 노드
                visited[next_node] = True
                prev[next_node] = now_node

                if next_node == end:
                    return prev

    return None


def find_path(prev, start, end):
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = prev[curr]

    path.append(start)
    path.reverse()
    return path


# 인접행렬 정리
MAP = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]

start = 0

end = 6

prev = bfs(MAP, 0, 6)

if prev is None:
    print("연결된 경로가 없음")

else:
    path = find_path(prev, start, end)
    print("가장 짧은 경로", path)