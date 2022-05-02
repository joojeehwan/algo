
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
def solution(h, w, blocks):

    #  검은색 1  : / 아무것도 없음: 0

    # 데이처 전처리
    MAP = [[0] * h for _ in range(w)]
    answer = []
    for blo in blocks:
        row, col = blo
        MAP[row][col] = 1

    # 높이에서 빈공간의 갯수 answer에 누적하기
    # 위에서 부터 아래로 왼쪽에서 오른쪽으로 탐색
    cnt = 0
    for i in range(h):
        for j in range(w):
            if MAP[j][i] == 1:
                continue
            cnt += 1
        answer.append(cnt)

    return answer