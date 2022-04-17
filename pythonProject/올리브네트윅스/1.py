
2
3
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
23
24
25
26
27
28
29
30
def solution(room):

    N = len(room)
    M = len(room[0])

    dirty_indexs = []
    new_room = []
    for i in range(N):
        for j in range(M):
            new_room.append(room[i][j])
            if room[i][j] == "$":
                dirty_indexs.append((i, j))

    print(dirty_indexs)
    answer = 0

    for dirty_idx in dirty_indexs:
        start_row, start_col = dirty_idx

        #더러운 인덱스 바로 아래 선반이면 바로 삭제 되고 cnt 증가
        if new_room[start_row][start_col] == "#":
            new_room[start_row - 1][start_col] = "."
            answer += 1

        #그게 아니면 선반위에까지 이동하고, idx를 처리
        new_room[start_row][start_col] = "."
        for next_row in range(start_row, N-1):
            if room[next_row + 1][start_col] == "#" :
                room[next_row][start_col] = "$"
    return answer