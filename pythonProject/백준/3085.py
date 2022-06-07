'''

간단하게 설명하면,
자리바꾸고 -> 탐색해서 최댓값 갱신
-> 자리원위치 -> 자리바꾸고
-> 탐색해서 최댓값 갱신
이 과정을 반복하면서 최댓값을 갱신해 주면 된다.



'''


import sys

input = sys.stdin.readline

#MAP에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수
def count(MAP):
    Max = 1 #최댓값을 구하니

    for i in range(n):
        #열(가로) 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if MAP[i][j] == MAP[i][j-1]:
                cnt += 1

            else:
                #이전과 다르다면 다시 1로 초기화
                cnt = 1
            Max = max(Max, cnt)

        cnt = 1
        for j in range(1, n):
            if MAP[j][i] == MAP[j-1][i]:
                cnt += 1

            else:
                cnt = 1

            Max = max(Max, cnt)

    return Max

n = int(input())
MAP = [list(input()) for _ in range(n)]
ans = 0

for i in range(n): #행
    for j in range(n): #열
        #열 바꾸기
        if j+1 < n:
            #인접한 것과 바꾼다
            MAP[i][j], MAP[i][j+1] = MAP[i][j+1], MAP[i][j]

            temp = count(MAP)
            ans = max(ans, temp)

            #바꿧던것 다시 원위치로!
            MAP[i][j], MAP[i][j+1] = MAP[i][j+1], MAP[i][j]

        #행 바꾸기
        if i+1 < n:
            #인접한 것과 바꾸기
            MAP[i][j], MAP[i+1][j] = MAP[i+1][j], MAP[i][j]
            temp = count(MAP)
            ans = max(ans, temp)
            #바꿧던 것을 다시 원래대로 돌랴놓기
            MAP[i][j], MAP[i+1][j] = MAP[i+1][j], MAP[i][j]

print(ans)


'''
import sys
input = sys.stdin.readline


def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        # 열(col) 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # for문을 돌면서 비교해 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

        # 행(row) 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer


n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # n보다 작으면 열을 바꿀 수 있다
        if j + 1 < n:
            # 인점한 것과 바꾸기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

            # check는 arr에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp = check(arr)

            if temp > answer:
                answer = temp

            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        #  n보다 작으면 행을 바꿀 수 있다
        if i + 1 < n:
            # 인점한 것과 바꾸기
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp = check(arr)

            if temp > answer:
                answer = temp

            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(answer)


'''