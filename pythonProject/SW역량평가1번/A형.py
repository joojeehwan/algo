import sys

from collections import deque

# BFS?!

sys.stdin = open("sample_input.txt", "r")

T = int(input())

def bfs(start, count, num):

    #2. 큐 생성
    q = deque([start])
    #일단은 순서대로 gate1 -> 2 ->3 의 순서대로 진행

    #3. 초기값 세팅
    MAP[start] = 1
    cnt = 1
    while q :

        if cnt == num:
            return
        
        #초기값 빼기
        now_point = q.popleft()

        cnt += 1
        #왼쪽 오른쪽 갈 수 있는 곳 탐색
        for i in [-1, 1]:
            next_point = now_point + i

            #범위 밖에 가지 못하게
            if next_point <= 0 or next_point > count :
                continue

            #이미 간곳은 가지 못하게
            if MAP == -1:
                continue
            q.append((next_point))
            MAP[next_point] = cnt

for t in range(1, T + 1):

    N = int(input())
    #1. MAP구성
    MAP = [-1] * (N + 1)

    #각각의 gate 입력받음
    gate1 = list(map(int, input().split()))
    gate2 = list(map(int, input().split()))
    gate3 = list(map(int, input().split()))
    bfs(gate1[0], N, gate1[1])
    print(MAP)

    # bfs(gate1[0], N)
    # print(MAP)



    #bfs 실행





