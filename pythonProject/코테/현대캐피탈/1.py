import math

def solution(passes, minutes):

    MIN = 987654321
    ans = 0
    for pa in passes:
        bp, bt, it, ap = pa
        if (minutes - bt) <= 0:
            ans = bp
        else:
            ans = bp + math.ceil((minutes - bt) / it) * ap

        MIN = min(ans, MIN)

    return MIN