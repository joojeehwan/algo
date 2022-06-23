def solution(penter, pexit, pescape, data):

    answer = ""
    N = len(penter)
    ans_lst = []
    list_data = list(data)

    # pescape 넣기
    while list_data:
        temp = []
        for _ in range(N):
            temp.append(list_data.pop(0))

        if temp == list(pescape):
            ans_lst.append(pescape)
            ans_lst.extend(temp)

        elif temp == list(penter):
            ans_lst.append(pescape)
            ans_lst.extend(temp)

        elif temp == list(pexit):
            ans_lst.append(pescape)
            ans_lst.extend(temp)

        else:
            ans_lst.extend(temp)

    #맨 앞과 뒤에 penter / pexit 넣기
    ans_lst.append(pexit)
    ans_lst.insert(0, penter)

    #ans_lst 정리
    for da in ans_lst:
        answer += da

    return answer


'''

쉽게 생각해야대는데,,
idx떄뭄ㄴ에 lst에서 뺴면서 하는게 훨씬 낫다,, insert로 하면 끝도 없다


'''