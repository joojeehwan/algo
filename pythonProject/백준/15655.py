'''


순서를 허용하지 말자!

'''




N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
visited = [False] * N
result = []

def dfs(lev, idx, N, M ):

    if lev == M:
        print(' '.join(map(str, result)))
        return

    for i in range(idx, N): #idx를 둠으러서 순서를 허용하지 않는다!
        if not visited[i]: #한번도 안 가본 곳
            visited[i] = True
            result.append(lst[i])
            #idx도 같이 증가 시켜야한다
            dfs(lev+1, idx+1, N, M)
            result.pop()
            visited[i] = False

dfs(0, 0, N, M)