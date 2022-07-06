def solution(n, m, x, y, z):
    # n : 노드
    # m : 간선
    INF = int(1e9)

    MAP = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                MAP[a][b] = 0

    # print(MAP)
    # 각 간선에 정보 => 초기화
    for i in range(m):
        MAP[x[i]][y[i]] = z[i]

    # print(MAP)
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                MAP[a][b] = min(MAP[a][b], MAP[a][k] + MAP[k][b])

    for a in range(1,  n + 1):
        for b in range(1, n + 1):
            if MAP[a][b] == INF:
                print("무한", end = " ")
            else:
                print(MAP[a][b], end=" ")
        print()

    answer = []
    return answer


print(solution(4, 4, [1,1,3,4], [3,4,2,2], [2,1,1,2]))