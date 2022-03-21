'''

경로 찾기

'''

# from collections import deque
#
#
# def bfs(start):
#     q = deque()
#     visitsed = [0] * n
#     q.append(start)
#     while q:
#         now = q.popleft()
#         for node in MAP[now]: #갈 수 있는 노드 검색
#             if not visitsed[node]: #그 전에 방문하지 않은 곳만
#                 visitsed[node] = 1
#                 q.append(node)
#
#     print(*visitsed)
#
# #와 인접행렬은 또 처음이네,, 항상 그냥 인덱스의 값이 이어진 행렬인것만 보다가
# #그래서 바꾸어 입력받기!
# n = int(input())
#
# MAP = [[] for _ in range(n)]
#
# for i in range(n):
#     arr = list(map(int, input().split()))
#     for w in range(n):
#         if arr[w]: #0같은 경우는 취급하지 않는다! 갈 수 있는 경우만 생각하겠다.
#             MAP[i].append(w) # 갈 수 있는 노드이니! append(w)를 하는 것!
#
#
# #모든 정점이니깐!
# for a in range(n):
#     bfs(a)


def dfs(lev): #깊이

    for i in range(n):
        if check[i] == 0 and arr[lev][i] == 1: #한번도 방문 하지 않았고, 1로 갈 수 있다는 표시가 있다면
            check[i] = 1 #방문했다고 표시하고
            dfs(i) # 그다음 칸을 향해 가자!


n = int(input())


arr = []

#진짜 문제 그대로 가져오기
for i in range(n):
    arr.append(list(map(int, input().split())))

check = [0 for _ in range(n)]
print(arr)