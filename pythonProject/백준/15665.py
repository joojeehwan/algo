
'''
N과 M(10)에서 비내림차순 조건을 제외하고, 같은 수를 출력해도 되는 문제



1. 비내림차순 조건을 위해 사용했던 idx로 range 조절 방법을 뺀다.
=> for문이 그래서 그냥 N인것 !

2. 같은 수를 여러 번 골라도 되므로 visited 방법을 뺀다.

4 4
1 1 2 2


1 1 1 1
1 1 1 2
1 1 2 1
1 1 2 2
1 2 1 1
1 2 1 2
1 2 2 1
1 2 2 2
2 1 1 1
2 1 1 2
2 1 2 1
2 1 2 2
2 2 1 1
2 2 1 2
2 2 2 1
2 2 2 2

'''

N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if overlap != L[i]:
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            out.pop()

solve(0, N, M)