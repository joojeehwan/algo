import math
from itertools import permutations


def is_prime_number(n):
    if n == 0 or n == 1:
        return False


    else:
        # 반만 가도 알 수 있고!
        for i in range(2, int(math.sqrt(n)) + 1):
            # 0이 되면 소수가 아니니깐!
            if n % i == 0:
                return False

        return True


def solution(numbers):
    answer = []

    # 조합의 경우의 수를 찾고!
    for i in range(1, len(numbers) + 1):
        lst = list(permutations(numbers, i))
        print(lst)
        # lst의 수만큼 숫자로 바궈서 -> isPrime 검사!
        for j in range(len(lst)):
            num = int("".join(lst[j]))
            print(num)
            if is_prime_number(num):
                answer.append(num)

    # 결국엔 중복제거!
    answer = list(set(answer))

    return len(answer)