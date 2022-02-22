def solution(clothes):
    closet = {}
    answer = 1

    # 같은 종류의 옷끼리 묶어서 사전에 저장
    for cloth in clothes:
        # 만약에 이미 closet안에 key값이 존재하면 append
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        # 그게 아니고 새로운 key라면 새롭게 다시 삽입
        else:
            closet[cloth[1]] = [cloth[0]]

    # {"종류" : ["옷 이름",,,]} 이런식으로 저장됨
    # 경우의 수 구하기
    for value in closet.values():
        answer *= len(value) + 1

    return answer - 1