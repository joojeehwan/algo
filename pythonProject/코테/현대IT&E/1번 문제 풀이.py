#BFS를 통해서 무리 나누기!


from collections import deque

answer = 0

def bfs(start_node, new_data, visited):
    global answer

    if visited[start_node] == True:
        return

    #초기값 설정
    q = deque()
    q.append((start_node))
    visited[start_node] = True
    while q:
        now_point = q.popleft()
        for next_point in new_data[now_point]:
            if not visited[next_point]:
                q.append((next_point))
                visited[next_point] = True
    answer += 1

def solution(V, bridge):
    # 데이터 전처리
    new_data = [[] for _ in range(V + 1)]
    for i in range(len(bridge)):
        new_data[bridge[i][0]].append(bridge[i][1])

    #방문 check 배열 만들기
    visited = [False] * (V + 1)

    #bfs 실행
    for node in range(1, V+1):
        bfs(node, new_data, visited)
    return answer - 1

