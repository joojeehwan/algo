'''

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

4 2
9 8 7 1

1 1
1 7
1 8
1 9
7 7
7 8
7 9
8 8
8 9
9 9

'''

N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(L[i])
        solve(depth+1, i, N, M) # 여기 i + 1을 안해서 같은 것을 허용! idx를 계속 늘리니깐 그래도 중복은 없다!
        out.pop()

solve(0, 0, N, M)


'''
n, m = map(int, input().split())
k = sorted(list(map(int, input().split()))) 
ans = [] 
def solve(depth, idx, n, m): 
    if depth == m: 
        print(' '.join(map(str, ans))) 
        return 
    for i in range(idx, n): 
        ans.append(k[i]) 
        solve(depth+1, i, n, m) 
        ans.pop() 

solve(0, 0, n, m)


'''