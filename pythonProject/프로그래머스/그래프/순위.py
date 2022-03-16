
'''

1.선수 A가 있을 때, A를 이긴 사람과 A에게 진 사람의 수를 합치면 N - 1이 되도록

2. A에게 진 사람은 A를 이긴 사람에게 반드시 진다. / A를 이긴 사람은 A에게 진 사람을 반드시 이긴다


bfs 여러번
https://sotchya.tistory.com/43
'''

from collections import deque


def solution(n, results):
    answer = 0

    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]

    for result in results:
        win[result[0]].append(result[1])
        lose[result[1]].append(result[0])

    # bfs 여러번 돌린것! 각 출발점에서 bfs돌린거라 생각 ,,!
    for i in range(1, n + 1):
        visited = [False for _ in range(n + 1)]
        visited[0] = visited[i] = True  # 0번은 그냥 안쓰니깐 한꺼번에 한 것!
        for nodes in [win, lose]:  # win , lose 순서대로 nodes에 넣고!
            q = deque([i])
            while q:
                idx = q.popleft()
                for node in nodes[idx]:
                    if not visited[node]:
                        visited[node] = True
                        q.append(node)

        if False not in visited:
            answer += 1
    return answer

# def solution(n, results):
#     # wins[key] = key가 이긴 사람들의 집합
#     # loses[key] = key가 이기지 못한 사람들의 집합
#     wins, loses = {}, {}
#     for i in range(1, n+1):
#         wins[i], loses[i] = set(), set()

#     for i in range(1, n+1):
#         for battle in results:
#             if battle[0] == i: # i의 승리. i가 이긴 사람들
#                 wins[i].add(battle[1])
#             if battle[1] == i: # i의 패배. i가 진 사람들
#                 loses[i].add(battle[0])
#         # i를 이긴 사람들 (loses[i]) => i에게 진 사람(wins[i])은 반드시 이긴다
#         for winner in loses[i]:
#             wins[winner].update(wins[i])
#         # i에게 진 사람들 (wins[i]) => i를 이긴 사람들(loses[i])에게는 반드시 진다
#         for loser in wins[i]:
#             loses[loser].update(loses[i])

#     cnt = 0
#     for i in range(1, n+1):
#         if len(wins[i]) + len(loses[i]) == n - 1:
#             cnt += 1
#     return cnt

#     return answer
