##stack으로 푸는,, 신기한 문제,,

from collections import defaultdict


def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():  ## 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 하는,,!
        routes[key].sort(reverse=True)

    print(routes["jjh"])
    stack = ["ICN"]

    while stack:
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())

    answer.reverse()
    return answer