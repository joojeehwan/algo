

# n, m = map(int, input().split())
#
#
#
# s = []
#
#
# def dfs():
#
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#
#     #중복을 확인하지 않는다!
#     for i in range(1, n+1):
#         s.append(i)
#         dfs()
#         s.pop()
#
# dfs()

'''
https://jiwon-coding.tistory.com/21님의 풀이 참고
n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()

'''

# N, M = map(int, input().split())
# out = []
#
# def solve(depth, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     for i in range(N):
#         out.append(i+1)
#         solve(depth+1, N, M)
#         out.pop()
#
# solve(0, N, M)


N, M = map(int, input().split())

lst = []

def dfs(lev, N, M):

    if lev == M:
        print(' '.join(map(str, lst)))
        return


    for i in range(1, N + 1):
        lst.append(i)
        dfs(lev + 1, N, M)
        lst.pop()

dfs(0, N, M)