import sys

T = int(input()) # 테스트 케이스

for i in range(T):

    cnt = 1
    people = []

    N = int(input())

    for i in range(N):
        paper, interview = map(int, sys.stdin.readline().split())
        people.append([paper, interview])
    people.sort(key = lambda x : x[0]) #서류 기준 오름차순 정렬
    MAX = people[0][1]

    print(people)

    for i in range(1, N):
        if MAX > people[i][1]: #서류를 피벗으로 인터뷰를 for문 돌리는거라 생각 / 점수가 높아야 합격할 수 있으니
            cnt += 1
            MAX = people[i][1] #여기 값을 업데이트 해야만


    print(cnt)
    


