
# 다른 사람 풀이, enumerate,, 사용 좋다
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result



#내 풀이


def solution(answers):
    #들어오는 문제랑 내가 찍는거랑 1대1로 비교!
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]

    count1 , count2, count3 = 0, 0, 0
    for i in range(len(answers)):
        #포인트! 늘어가는 i 값에 따라 반복되는 주기 만큼 다시 i값이 변화해야 하니깐!
        #a list의 범위 안에서 돌 수 있도록
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10

        if a1[s1] == answers[i]:
            count1 += 1
        if a2[s2] == answers[i]:
            count2 += 1
        if a3[s3] == answers[i]:
            count3 += 1

    k = max(count1, count2, count3)
    answer = []

    if k == count1:
        answer.append(1)
    if k == count2:
        answer.append(2)
    if k == count3:
        answer.append(3)
    return answer