#1단계 백트래킹 기본 틀 잡기

'''

nums: 숫자들을 담은 리스트
arr: 정답 리스트
visited: 중복 제거를 위한 사용여부 boolean 리스트
former: 중복 정답 제거를 위한 이전 숫자 기억 변수

'''


#1단계 기본틀
def dfs():

    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(n):
        arr.append(nums[i])
        dfs()
        arr.pop()

'''
# 입력
4 2
9 7 9 1

# 출력
1 1
1 7
1 9
1 9
7 1
7 7
7 9
7 9
9 1
9 7
9 9
9 9
9 1
9 7
9 9
9 9

'''

#2단계 사용하지 않은 곳만 간다.

def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        if not visited[i]:
            arr.append(nums[i])
            visited[i] = True
            dfs()
            arr.pop()
            visited[i] = False


'''
# 입력
4 2
9 7 9 1

# 출력
1 7
1 9
1 9
7 1
7 9
7 9
9 1
9 7
9 9
9 1
9 7
9 9

'''

#3단계  같은 숫자가 여러 번 등장하는 리스트의 경우 9가 포함된 조합이 여러 번 출력되는 것을 막아야 한다.
def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    former = 0
    for i in range(n):
        if not visited[i] and nums[i] != former:
            arr.append(nums[i])
            visited[i] = True
            former = nums[i]
            dfs()
            arr.pop()
            visited[i] = False


'''
# 입력
4 2
9 7 9 1

# 출력
1 7
1 9
7 1
7 9
9 1
9 7
9 9


'''

#4단계 마지막으로, 비내림차순으로 만들어주어야 한다.
# dfs 함수에 idx 파라미터를 추가해서 재귀함수에 현재 인덱스를 넘겨주고 해당 재귀함수에서 현재 인덱스+1의 위치부터 탐색을 시작하도록 한다.

def dfs(idx):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    former = 0
    for i in range(idx + 1, n):
        if not visited[i] and nums[i] != former:
            arr.append(nums[i])
            visited[i] = True
            former = nums[i]
            dfs(i)
            arr.pop()
            visited[i] = False


dfs(-1)


'''
# 입력
4 2
9 7 9 1

# 출력
1 7
1 9
7 9
9 9

'''


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []
visited = [False] * n

# dfs(-1)