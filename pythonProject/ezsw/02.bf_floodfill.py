

#flood fill 알고리즘


def fill(r, c):
    
    #범위 밖
    if r < 0 or r > n - 1 or c < 0 or c > n -1 :

        return

    if MAP[r][c] != 0:
        return

    MAP[r][c] = 1
    fill(r - 1, c)
    fill(r + 1, c)
    fill(r, c - 1)
    fill(r, c + 1)


n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

start_row, start_col = map(int, input().split())

fill(start_row , start_col)

for i in range(n):
    for j in range(n):
        print(MAP[i][j], end = ' ')
    print()

