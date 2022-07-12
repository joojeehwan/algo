'''

링크와 스타트

'''


def isIt():
    global answer
    pow1, pow2 = 0, 0
    for i in range(n):  # 이중 포문을 돌려서 i,j // j,i를 둘다 인덱스에 넣을 수 있게
        for j in range(n):
            # 방문한 곳은 스타트팀!
            if visited[i] and visited[j]:
                pow1 += MAP[i][j]
            elif not visited[i] and not visited[j]:
                pow2 += MAP[i][j]
    answer = min(answer, abs(pow1 - pow2))
    return

#조합을 뽑아 내기 위한 과정
def resolve(iter):
    if iter == n:
        isIt()
        return
    visited[iter] = True
    resolve(iter + 1)
    visited[iter] = False
    resolve(iter + 1)





n = int(input())

visited = [False for _ in range(n)]
MAP = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9

resolve(0)
print(answer)


