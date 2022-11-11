
# 와 이렇게 사용이 가능하네?!
def test() :

    for i in range(3):
        temp = i

    return temp

print(test()) # 2


# 활용

from collections import deque

N = 5

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

MAP = [list(map(int, input().split())) for _ in range(N)]


def bfs_destination(person_start_row, person_start_col, person_end_row, person_end_col) :
    q = deque()
    q.append((person_start_row, person_start_col))
    visited = [[0] * N for _ in range(N)]

    while q:
        now_row, now_col = q.popleft()

        #지금 온 곳이, 바로 도착지라면 ?!
        if (now_row, now_col) == (person_end_row, person_end_col) :
            break

        for k in range(4):
            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            # 범위 안에 있고
            if 0 <= next_row < N and 0 <= next_col < N :
                # 한 번도 가지 않은 곳 이면서, 벽이 아닌 곳
                if not visited[next_row][next_col] and MAP[next_row][next_col] != 1 :
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    q.append((next_row, next_col))

    #while문이 끝났을 때의 now_row, now_col을 이런식으로 return이 가능
    #여기에 있는 now_row, now_col이 사용 가능한 것
    return visited[now_row][now_col], now_row, now_col