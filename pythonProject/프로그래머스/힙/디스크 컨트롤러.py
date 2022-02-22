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
            answer += (now - current[1])  # 작업 요청시간 부터 종료시간까지의 시간 계산
            i += 1
        else:
            now += 1

    return int(answer / len(jobs))


'''
바로 이전에 작업을 완료한 시간(start)보다 크고 현재 시점(now)보다 작으면 현재 시점에서 처리할 수 있는 작업이 됩니다. 
현재 시점에서 처리할 수 있는 작업을 heap에 저장합니다. 이 때 소요시간 기준으로 최소힙을 사용하기 때문에 heap에 저장할 때 [작업 소요 시간, 작업 요청 시간] 으로 저장합니다. 
heap의 길이가 0보다 크다면 처리할 작업이 있는 경우이므로 작업 요청시간부터 종료시간까지 계산하고 다음 작업으로 넘어갈 수 있도록 start 와 now 값을 바꾸어줍니다. 
heap의 길이가 0이라면 처리할 작업이 없는 경우이므로 현재 시점을 다음 시간으로 넘어가기 위해 now에 1을 더해줍니다. 마지막에는 평균 시간은 리턴해주면 됩니다

'''
#제일 좋은건 파이선 튜터 돌려보면 코드의 흐름을 알 수 있다.