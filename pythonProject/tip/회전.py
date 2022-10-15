

#반 시계
MAP = [[1,2,3], [4,5,6], [7, 8, 9]]

n = 3
temp = [[0] * 3 for _ in range(3)]

for row in range(3):
    for col in range(3):

        temp[n - 1 - col][row] = MAP[row][col]


MAP = temp[:]

print(MAP)


# 시계 방향
MAP = [[1,2,3], [4,5,6], [7, 8, 9]]

n = 3
temp = [[0] * 3 for _ in range(3)]

for row in range(3):
    for col in range(3):

        temp[col][n - 1 - row] = MAP[row][col]


MAP = temp[:]

print(MAP)
