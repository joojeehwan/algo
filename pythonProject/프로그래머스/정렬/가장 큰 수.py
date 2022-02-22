def solution(numbers):
    temp = list(map(str, numbers))

    # str을 사전순으로 정렬하면! 그 숫자의 크기는 상관없다!
    '''
    3을 곱하는 이유는 2번째 예시를 풀 때 이유를 알게 된다.
계산할 때 사전값으로만 정렬을 한다면 [9,5,34,30,3] 이렇게 정렬된다.
하지만 3이 30보다 앞에 와야한다.
number는 1000이하의 숫자이므로 최대값을 생각해 3을 곱해줬고,
3을 곱하게 되면 [999, 555, 343434, 303030, 333] 이렇게 될 것이고, 정렬을 하게 되면 [999, 555, 343434, 333, 303030]이 된다.

    '''
    temp.sort(key=lambda x: x * 3, reverse=True)

    answer = str(int("".join(temp)))
    return answer