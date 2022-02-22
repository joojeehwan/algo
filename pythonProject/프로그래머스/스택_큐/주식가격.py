def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer

prices = [1,2,3,2,3]
de = 1
print(solution(prices))

from collections import deque

def solution(prices):

    queue = deque(prices)

    answer = []
    while queue:
        price = queue.popleft()
        count = 0
        for q in queue:
            count += 1
            if price > q: #price보다 작아진 q를 만나면 멈처야지! 증가시키는 것을! 그래야!
                break
        answer.append(count)
    return answer


#이중 포문을 돌리는게 아니라 ,, queue로 => 효율성 제로
def solution(prices):

    answer = [0] * len(prices)
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
