def solution(nums):
    answer = 0
    length = len(nums) // 2
    # 집합으로 중복을 없애고, 다시 배열로 만듬.
    temp = list(set(nums))
    print(temp, length)

    for num in temp:
        if answer < length:
            answer += 1
    return answer