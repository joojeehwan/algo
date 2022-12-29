# 조합 ver1

lst = [1, 2, 3, 4, 5]

target = 2

n = len(lst)

answer = []


def dfs(now_node, temp):
    if len(temp) == target:
        answer.append(temp[:])
        return

    for next_node in range(now_node, n):
        # ver1 - 1
        # temp.append(lst[next_node])
        # dfs(next_node + 1, temp)
        # temp.pop()

        # ver1 - 2
        dfs(next_node + 1, temp + [lst[next_node]])


dfs(0, [])
print(answer)

# 조합 ver2

lst = [1, 2, 3, 4, 5]

target = 2

n = len(lst)

answer = []


def dfs_2(lev, cnt, temp):
    # if cnt == target:
    #     return answer.append(temp[:])

    # if lev == n:
    #     return

    # 전체를 다 돌고
    if lev == n:

        # 해당 경우의 수의 요소의 갯수가, 내가 찾고자 하는 경우의 수 갯수와 같다면
        if cnt == target:
            answer.append(temp[:])

        return

    temp.append(lst[lev])
    dfs_2(lev + 1, cnt + 1, temp)
    temp.pop()
    dfs_2(lev + 1, cnt, temp)


dfs_2(0, 0, [])
print(answer)


# 순열 ver1

lst = [1,2,3,4,5]

target = 2

n = len(lst)

visited = [False] * n

answer = []

def dfs(lev, temp):

    if lev == target:

        answer.append(temp[:])

    #조합과의 가장 큰 차이점.. 모든 것을 다 본다. 그래서 visted 배열로 체킹이 필요 한 것
    for next_lev in range(n) :

        if not visited[next_lev] :

            visited[next_lev] = True
            temp.append(lst[next_lev])
            dfs(lev + 1, temp)
            visited[next_lev] = False
            temp.pop()

dfs(0, [])

print(answer)

# 순열 ver2 비트마스킹

lst = [1,2,3,4,5]

target = 2

n = len(lst)

answer = []


def dfs_v2(lev, used, temp):

    if lev == target:
        return answer.append(temp[:])

    for i in range(n):

        # i 값을 변화시키면서, used 숫자와의 & 연산을 통해 이용여부를 판단
        # 이용o 1 & 1 = 1 // 이용x 0 & 1 = 0 이렇게
        if used & (1 << i) :
            continue

        temp.append(lst[i])
        dfs_v2(lev + 1, used | (1 << i), temp)
        temp.pop()


dfs_v2(0, 0, [])

print(answer)


