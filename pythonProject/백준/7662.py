'''

이중 우선순위 큐


I N : N의 숫자를 큐에 넣어라

D 1 : 최댓값을 없애라
D -1 : 최솟값을 없애라
최댓값(최솟값)이 둘 이상인 경우, 하나만 삭제됨

'''


import sys;read=sys.stdin.readline
import heapq

result=[]
for T in range(int(read())):
    visited=[False]*1_000_001
    minH,maxH=[],[]
    for i in range(int(read())):
        s=read().split()
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))
            visited[i]=True
        elif s[1]=='1':
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]]=False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
    result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')
print('\n'.join(result))




import heapq

t = int(input())

for i in range(t):
    k = int(input())
    q1, q2 = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()

        if com == 'I':
            heapq.heappush(q1, (int(num), j))
            heapq.heappush(q2, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else:
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)

    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    if not q1 or not q2:
        print("EMPTY")
    else:
        a = -q2[0][0]
        b = q1[0][0]
        print("%d %d" % (a, b))

import heapq


def sync(arr):
    while arr and id[arr[0][1]] == 0:
        heapq.heappop(arr)


T = int(input())
for test_case in range(T):
    max_arr = []
    min_arr = []
    id = [0] * 1000000
    K = int(input())
    count = 0
    for i in range(K):
        S, num = input().split()

        if S == "I":
            heapq.heappush(max_arr, (-1 * int(num), i))
            heapq.heappush(min_arr, (int(num), i))
            id[i] = 1

        else:

            if num == "1":
                sync(max_arr)
                if max_arr:
                    id[max_arr[0][1]] = 0
                    heapq.heappop(max_arr)

            elif num == "-1":
                sync(min_arr)
                if min_arr:
                    id[min_arr[0][1]] = 0
                    heapq.heappop(min_arr)

    sync(max_arr)
    sync(min_arr)


    if len(max_arr) == 0:
        print("EMPTY")
    else:
        print(-1 * max_arr[0][0], end =" ")
        print(min_arr[0][0])