'''

가장 큰 두수의 합 구하기

'''

n = 3

lst = [1, 2, 3]


def solve(lev, cnt, res):

    if cnt == 2:
        return res

    if lev == n:
        return -1


    ret = 0
    '''
    하나의 레벨에서 있고 있고 있고 가보고 다시 돌아와서 없고 없고를 가보는! 그래서 한 레벨마다
    있고 없고의 경우를 나누어서!!
    어제 손으로 직접 써가면서 느꼈듯이, "한 레벨"에서 아래의 두 줄의 코드가 이루어지니깐!! 재귀지만! 분명히 아래 두줄은
    같은 충위에 있어
    '''
    ret = max(ret, solve(lev + 1, cnt + 1, res + lst[lev]))
    ret = max(ret, solve(lev + 1, cnt, res))

    return ret



print(solve(0, 0, 0))

