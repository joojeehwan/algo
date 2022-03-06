def solution(N, number):
    answer = 0
    # 4칙연산을 하지 않았을 떄, 당연시 생각할 수 있는 수들의 조합(N, NN, NNN)와 같은 것들
    dp = [set([N * int("1" * i)]) for i in range(1, 9)]

    for i in range(8):
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i - j - 1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 / num2)

        if number in dp[i]:
            return i + 1

    return -1


from math import inf

answer = inf


def dfs(n, cnt, num, number):
    global answer

    if answer < inf and cnt > answer:
        return

    if cnt > 8:
        return

    if num == number:
        answer = min(answer, cnt)
        return

    next_num = 0
    for i in range(8):
        next_num = next_num * 10 + n
        dfs(n, cnt + 1 + i, num + next_num, number)
        dfs(n, cnt + 1 + i, num - next_num, number)
        dfs(n, cnt + 1 + i, num * next_num, number)
        dfs(n, cnt + 1 + i, num / next_num, number)


def solution(N, number):
    dfs(N, 0, 0, number)
    return -1 if answer == inf else answer


