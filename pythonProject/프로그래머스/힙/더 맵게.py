import heapq


def solution(scoville, K):
    answer = 0


# #스코빌 지수가 k이상인지 확인
# def check_sco(sco_lst, k):
#     for sco in sco_lst:
#         if sco < k :
#             return True

#         else:
#             return False

# def solution(scoville, K):

#     heap = []
#     for sco in scoville:
#         heapq.heappush(heap, sco)
#     count = 0
#     scope = len(heap) + 1
#     while scope:
#         if(check_sco(heap, K)):
#             # 스코빌 지수가 k 이하인게 있으니 작업실행
#             count += 1
#             nothot_first = heapq.heappop(heap)
#             nothot_second = heapq.heappop(heap)
#             new_sco = nothot_first + (nothot_second * 2)
#             heapq.heappush(heap, new_sco)
#         else:
#             return count

#     return -1


# 풀이 1
def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)  # list to heapq

    while scoville[0] < K:  # 가장 작은 수가 기준보다 낮다면 계속
        if len(scoville) > 1:
            answer += 1
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
        else:
            return -1
    return answer


# 풀이 2

import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1

    return answer