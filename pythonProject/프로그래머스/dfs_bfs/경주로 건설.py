from collections import deque


def solution(board):
    dX = [1, -1, 0, 0]
    dY = [0, 0, 1, -1]
    queue = deque([])
    queue.append((0, 0, 0, 0))  # 좌표, 방향
    valueBoard = list([0] * len(board) for _ in range(len(board)))

    while queue:
        x, y, car_d, value = queue.popleft()
        for road_d in range(4):  # 동 서 남 북 방향
            nX = x + dX[road_d]
            nY = y + dY[road_d]

            if 0 <= nX < len(board) and 0 <= nY < len(board):
                if board[nY][nX] != 1:
                    if nX == 0 and nY == 0:
                        continue

                    if x == 0 and y == 0:
                        newValue = value + 100
                    else:
                        if car_d == road_d:
                            newValue = value + 100
                        else:
                            newValue = value + 600

                    if valueBoard[nY][nX] == 0:
                        valueBoard[nY][nX] = newValue
                        queue.append((nX, nY, road_d, newValue))
                    else:
                        if valueBoard[nY][nX] >= newValue:
                            valueBoard[nY][nX] = newValue
                            queue.append((nX, nY, road_d, newValue))

    return valueBoard[-1][-1]


import math
from collections import deque


def solution(board):
    def bfs(start):

        # table[y][x] = 해당 위치에 도달하는 최솟값
        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]

        # 진행 방향 위 0 , 왼쪽 1 , 아래 2, 오른쪽 3
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = deque([start])
        # 초기 비용은 0
        table[0][0] = 0
        while q:
            # row, col , 비용, 진행방향
            row, col, cost, head = q.popleft()
            for idx, (dr, dc) in enumerate(dirs):
                next_row = row + dr
                next_col = col + dc

                # 진행방향과 다음 방향이 일치하면 + 100, 다르면 전환비용 500 + 진행비용 100 = 600

                next_cost = cost + 600 if idx != head else cost + 100

                if 0 <= next_row < len(board) and 0 <= next_col < len(board) and board[next_row][next_col] == 0 and \
                        table[next_row][next_col] > next_cost:
                    table[next_row][next_col] = next_cost
                    q.append((next_row, next_col, next_cost, idx))

        return table[-1][-1]

    return min(bfs((0, 0, 0, 2)), bfs((0, 0, 0, 3)))


