'''

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

예제 입력 1
3 1
4 4 2

예제 출력 1
2
4


예제 입력 2
4 2
9 7 9 1

예제 출력 2
1 1
1 7
1 9
7 7
7 9
9 9


예제 입력 3
4 4
1 1 2 2

예제 출력 3
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2
'''

# def dfs(lev):
#
#     if lev == M:
#         #arr을 하나하나 str으로 바꿔서! join으로 문자열 합치기!
#         print(" ".join(map(str, arr)))
#         return
#
#     for i in range(len(nums)):
#         if lev == 0 or arr[-1] <= nums[i]:
#             arr.append(nums[i])
#             dfs(lev + 1)
#             arr.pop()
#
# N, M = map(int, input().split())
# #정렬하고, 처음부터 set으로해서 중복 x
# nums = sorted(list(set(map(int, input().split()))))
#
# # print(nums)
#
# arr = []
# dfs(0)

N, M = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))

ans = []
p = []

def dfs(lev, idx):
    if lev == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(idx, len(nums)):
        ans.append(nums[i])
        dfs(lev + 1, i)
        ans.pop()

dfs(0, 0)


