'''


그리디 알고리즘


'''


n = int(input())
heights = list(map(int, input().split()))

ans = [0] * n

#실제 숫자들은 1부터 시작하니...!
for i in range(1, n + 1):

    temp = heights[i-1]
    cnt = 0

    for j in range(n):
        if cnt == temp and ans[j] == 0:
            ans[j] = i
            break
        elif ans[j] == 0:
            cnt += 1

print(*ans)


for i in range(1, n + 1):

    temp = heights[i - 1]
    cnt = 0

    for j in range(n):
        if cnt == temp and ans[i] == 0:
            ans[j] = i
            break
        elif ans[i] == 0:
            cnt += 1