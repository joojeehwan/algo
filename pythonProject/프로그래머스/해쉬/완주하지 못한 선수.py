# 파이썬에 hash함수가 있구나,,!

# def solution(participant, completion):
#     answer = ""
#     temp = 0
#     ddic = {}
#     for part in participant:
#         ddic[hash(part)] = part
#         temp += int(hash(part))

#     for com in completion:
#         temp -= int(hash(com))
#     #temp에 혼자 남은 그 완주하지 못한 그 사람의 해시값만이 남아 있는다!
#     answer = ddic.get(temp)
#     return answer


# 이름을 key값으로 해보자!
def solution(participant, completion):
    ddic = {}
    # 이렇게 수를 넣어서 표식을 할 수 있다는 생각을 왜 못하지!! 해보자!!
    for parti in participant:
        if parti in ddic:
            ddic[parti] += 1  # 동면이인인 경우

        else:
            ddic[parti] = 1  # 그대로 그냥 들어온 경우!

    # 완주자 이름(key)의 value가 1이면 지우기, 동면이인이면 -1

    for com in completion:
        if ddic[com] == 1:
            del ddic[com]
        else:  # 동명이인인 경우
            ddic[com] -= 1

    # 객체로 반환되니깐! keys()로 dict의 key였던 이름을 배열로 받아서 값 하나 반환
    return list(ddic.keys())[0]