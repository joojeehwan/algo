'''


어렵게 생각할 거 없이 주어지는 명함마다 큰 수와 작은 수를 분류해서,
큰 수는 큰 수끼리 작은 수는 작은 수끼리 비교한 것 중 가장 큰 값을 각각 뽑은뒤 곱해주면 된다!

'''


def solution(sizes):
    big = []
    small = []
    answer = 0
    for namecard in sizes:
        if namecard[0] > namecard[1]:
            big.append(namecard[0])
            small.append(namecard[1])

        else:
            big.append(namecard[1])
            small.append(namecard[0])
    answer = max(big) * max(small)

    return answer


