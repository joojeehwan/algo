
'''

우선 str.startswith(str or tuple) 형식으로 사용하면 되고,
반환 값으로는 True, False를 반환한다.

'''


# 대소문자 구별함

string = "hello startswith"
print(string.startswith("hello"))


string = "hello startswith"
print(string.startswith("Hello"))


# input으로 str이나 str로 이루어진 tuple이 옴
string = "hello startswith"
tuple_string = ("hello", "bye")
print(string.startswith(tuple_string))