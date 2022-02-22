''''

그냥 문자열끼리도 대소 비교 된다. 굳이 정수형으로 바꿀 필요 x


'''


def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])