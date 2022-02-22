def solution(priorities, location):
    loc = [i for i in range(len(priorities))]  # 위치 정보,,!
    answer = []

    print(loc)

    while len(priorities) != 0:
        if priorities[0] == max(priorities):  # 맨 앞에 것이 최고 우선순위이면, 답에 넣는다
            answer.append(loc.pop(0))  # pop해서 빼서 넣기
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))  # 뒤로 돌려놓기! 뺴서 돌려넣기
            loc.append(loc.pop(0))  # 뒤로 돌려놓기! 뺴서 돌려넣기

    return answer.index(location) + 1

