# 1
# print(-1 % 8) # 값이 양수 7 나온다.


# 마법사 상어와 복제 문제 다시 보기
# 2
# https://stackoverflow.com/questions/44714705/python-access-global-list-in-function
# 복사할 때는, global로 해서 가져와야 한다.

def func(lst):
    res = []
    global test
    #global로 가져오면 여기서 또 에러 나네
    test[0] = 1

    #밑에 복사가 들어가면, 오류가 난다. ... 왜그러는걱지?!
    #test = lst[:]

    return res

test = []
temp = func([1,2,3,4,5])
