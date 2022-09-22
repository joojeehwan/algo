# 완전 탐색 - 순열 (순서o)

# 배열에서 가장 큰 두 자리 수 구하기.


n = 4

lst = [1,2,3,4]

'''
순열 서로 다른 n개 중에 r개를 뽑아 한줄로 나열(순서가 의미 있음.)


cnt : 숫자 개수 제한
used : 선택된 원소에 대한 비트 정보 

'''
def permutaion(cnt, used, res) :

    if cnt == 2:
        return res
    print(used)
    ret = 0
    for i in range(n):
        #가로가 없더라도 비트연산이 우선순위가 더 높다.
        # used가 1이야 0이야?! 를 판단 =? 너 이미 간곳이야?! 아니면 안간곳이야?! 를 판단.
        if used & (1 << i) :
            continue
        #used | (1 << i) : vistied의 배열에서 false인 부분을(안 가본 곳)을 True로 바꿔주는 부분
        # |(or) 연산을 통해서 안에 값을 표시 하는 행위
        ret = max(ret, permutaion(cnt + 1, used | (1 << i) , res * 10 + lst[i]))


    return ret

print(permutaion(0, 0, 0))
