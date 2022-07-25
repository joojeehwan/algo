from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for p in permutations(dungeons, len(dungeons)):

        tmp = k  # 지속적으로 for문이 돌면서 피로도를 입력받는다.
        cnt = 0  # cnt를 세기 위해서!

        # 나올 수 있는 가짓수 중 하나에서 직접 피로도 연산을 진행
        for need, spend in p:
            # 조건1 최소 필요 피로도보다 지금 내 피로도가 더 많고
            if tmp >= need:
                tmp -= spend
                cnt += 1
        answer = max(answer, cnt)

    return answer

    return answer

#dfs 풀이 - 이정도 풀줄 알아야 한다.

answer = 0


def dfs(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):

        # 한번도 가지 않은 곳 이고 and 최소 필요 피로도를 만족
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer