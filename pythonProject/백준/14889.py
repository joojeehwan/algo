'''

스타트와 링크

dfs(백트래킹)

https://developer-ellen.tistory.com/50?category=879172

1. 스타트와 링크 두 팀으로 나누기 위하여 한 팀에 속하면 visited 리스트를 통하여 방문처리 해주면서 재귀함수 형태로 만든다.

2. 만약 한 팀에 속한 팀원의 명수가 n//2로 다 채워졌으면 스타트팀의 능력치와 링크팀의 능력치를 구한다.

3. 방문처리된 팀이 스타트팀이라고 하면, 방문처리 안된 팀이 링크팀이다. 이것을 이용해서 능력치를 구할 수 있다.

4. 스타트팀의 능력치와 스타트팀의 능력치의 차이의 절대값과 최소 능력치값을 비교하면서 계속 갱신해준다.

'''


# def dfs(lev, idx):
#     global answer
#     #재귀 종료 조건 -> 팀에 속하 인원이 n // 2명이 다 되면
#     if lev == n // 2:
#         pow1, pow2 = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 #방문한 곳은 스타트팀!
#                 if visited[i] and visited[j]:
#                     pow1 += MAP[i][j]
#                 elif not visited[i] and not visited[j]:
#                     pow2 += MAP[i][j]
#         answer = min(answer, abs(pow1 - pow2))
#         return
#
#     #재귀 도는 부분, idx를 증가하면서 중복을 허락하지 않게 되는것! 1,2랑 2,1은 같은것!
#     for i in range(idx, n):
#         if not visited[i]:
#             visited[i] = True
#             dfs(lev + 1, i + 1)
#             visited[i] = False
#
#
# n = int(input())
#
# visited = [False for _ in range(n)]
# MAP = [list(map(int, input().split())) for _ in range(n)]
# answer = int(1e9)
#
# dfs(0, 0)
# print(answer)


#dfs 재귀 사용해서 하는게 아닌 방법


from itertools import combinations #조합 함수 사용

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

#조합 사용하여 가능한 팀의 경우의 수 만들기!
for team in list(combinations(members, N // 2)):
    possible_team.append(team)

# print(possible_team)

min_pow = int(1e9)

#전체의 반절만해도 팀 반으로 나눌 수 있으니
for i in range(len(possible_team) // 2):

    #A팀
    team = possible_team[i]
    # team 자체는 (0, 1)이런 형태 
    pow1 = 0
    for j in range(N // 2):
        member = team[j] #1, 2 // 2, 1이거 둘다 할려고
        for k in team: 
            pow1 += MAP[member][k] #이렇게 해도 되는 이유가 어차피 주대각선은 0으로 이루어져 있음

    team = possible_team[-i-1]
    pow2 = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            pow2 += MAP[member][k]

    min_pow = min(min_pow, abs(pow1 - pow2))


print(min_pow)


