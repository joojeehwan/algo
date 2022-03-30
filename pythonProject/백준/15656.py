

def dfs(lev):


    if lev == M:
        print(*lst)
        return

    for i in range(N):
        lst.append(Numbers[i])
        dfs(lev + 1)
        lst.pop()


N, M = map(int, input().split())
Numbers = list(map(int, input().split()))
lst = []
Numbers.sort()

dfs(0)