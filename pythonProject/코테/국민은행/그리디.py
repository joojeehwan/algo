'''

디스크 컨트롤러

'''

import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 할 수 있는 일들을 haep에 넣기
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        # 처리할 작업이 있다면
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]  # 작업 시간을 더한다 now에다가
            answer += (now - current[1])
            i += 1
        else:
            now += 1

    return int(answer / len(jobs))



#deque까지 써서 하는 풀이

import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)


#수정해야할 내 풀이

from collections import deque

def solution(times, n):

    vehicle = [0] * n
    total_time = 0
    q = deque(times)

    # 첫 번째 사람 탑승
    vehicle[0] = q.popleft()

    while True :

        if not q:
            break
        #관람차 한번 도는 것을 한번의 루틴

        now_time = q.popleft()
        # 전부 탑승
        for i in range(n):

            if not vehicle[i]:

                vehicle[i] = now_time
                total_time += 1
            else:
                vehicle[i] -= 1
                if vehicle[i] < 0:
                    vehicle[i] = 0
        #전부 탑승하고 이용
        for i in range(n):
            if not vehicle[i] :
                vehicle[i] -= 1

            else:

                total_time += 1

    return total_time