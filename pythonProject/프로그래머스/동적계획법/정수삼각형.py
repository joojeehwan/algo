def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:  # 왼쪽끝
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:  # 오른쪽 끝
                triangle[i][j] += triangle[i - 1][j - 1]
            else:  # 그 외
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    # 마지막 행의 최댓값을 구해라
    print(max(triangle[-1]))

    return max(triangle[-1])


def solution(triangle):
    answer = 0
    # 아 밑에 처럼 적을 수가 있그나,,
    #양옆으로 0을 넣어주네
    triangle = [[0] + t + [0] for t in triangle ]
    for i in range(1, len(triangle)):
        for j in range(1, i + 2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(triangle[-1])
    return answer