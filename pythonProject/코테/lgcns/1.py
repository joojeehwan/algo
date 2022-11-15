''''

1.

변경 전:

시소의 받침대를 기준으로 왼쪽에 위치한 구슬들의 무게의 합과 오른쪽에 위치한 구슬들의 무게의 합이 같아야 합니다. 중앙에 놓인 구슬이 있다면 무게를 계산할 때 제외합니다.

==>

변경 후, '좌우' 추가:

시소의 받침대를 기준으로 왼쪽에 위치한 구슬들의 무게의 합과 오른쪽에 위치한 구슬들의 무게의 합이 같아야 합니다. 중앙에 놓인 구슬이 있다면 좌우 무게를 계산할 때만 제외합니다.

2.

변경 전:

장식에 사용된 구슬의 무게들을 왼쪽부터 순서대로 담아 만든 배열이 사전 순으로 더 빠른 장식이 더 아름답습니다.

==>

변경 후, 괄호 부분 추가:

장식에 사용된 구슬의 무게들을 왼쪽부터 순서대로 담아 만든 배열이 사전 순으로 더 빠른 장식이 더 아름답습니다.

(첫번째 원소부터 순서대로 비교해서 작은 원소가 먼저 나오거나 비교할 원소가 먼저 바닥난 배열이 사전순으로 더 빠른 배열입니다.)


'''


from itertools import permutations
import copy

def checkMarbles(marbles, candidate, N):
    temps = list(permutations(marbles, N))
    for temp in temps:
        if sum(temp[0:(N) // 2]) == sum(temp[(N) // 2: N]):
            candidate.add(temp)

def solution(marbles) :

    #1. 전체 경우의 수 구하기
    candidate = set()
    N = len(marbles)
    real_marbles = copy.deepcopy(marbles)
    answer = []
    for _ in range(N):
        marbles.pop()
        debug = 1
        if len(marbles) == 0:
            break
        # 짝수개
        if len(marbles) % 2 == 0:
            checkMarbles(marbles, candidate, len(marbles))
        # 홀수개
        else:
            if len(marbles) == 1:
                for marble in real_marbles :
                    candidate.add(marble)
            for i in marbles[:]:
                marbles.remove(i)
                checkMarbles(marbles, candidate, len(marbles))
                marbles.insert(0, i)

    #2. 조건으로 비교하기
    for candi in candidate:
        if len(answer) == 0:
            answer.append(candi)

    return answer


solution([1,2,3,4,4])

