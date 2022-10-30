

from collections import deque

'''
1 -> 2 -> 3 -> 1

4 3 1
1 2
2 3
3 1

답은 4
'''


# 노드 개수 N 경로의 개수 M, 초기 시작 위치
# M개줄에 이어서 경로 구성 설명,
N, M, K = map(int, input().split())

MAP = [[] for _ in range(N - 1)]

#초기 입력
for _ in range(M):
    start, end = map(int, input().split())
    MAP[start - 1].append(end - 1)

#기록 배열...병신아... 1차원 배열로 했어야지..! 너 진짜 뒤지고 싶엉?!?!?!?!
visited = [False] * N
cnt = 0

def bfs():

    q = deque()
    q.append(K-1)
    global cnt

    flag = False
    while q:
        start_node = q.popleft()
        debug = 1

        if start_node == K - 1 and flag:
            cnt += 1
            return True

        for next_node in MAP[start_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                cnt += 1
                flag = True

    return False

if bfs() == False:
    print(-1)

else:
    print(cnt)




    