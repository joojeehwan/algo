'''

파이썬에서 리스트의 요소를 뒤집을 떄 사용.


'''



# reverse는 list 타입에서 제공하는 함수.
# 값을 반환하지 않고, 단순히 해당 list를 뒤집어 준다.

l = ["a", "b", "c"]

l.reverse()

print(l)


# reversed 내장함수, list에서 제공하는 함수가 아니다.
# 따라서, 굳이 리스트가 아니여도 다른 자료형도 가능하다!

l = ['d', 'e', 'f']
t = ('d', 'e', 'f')
s = 'def'

print(list(reversed(l)))
print(list(reversed(t)))
print(list(reversed(s)))

# 문자열을 만들려면 map을 활용해보자

l = ['a', 'b', 'c']

"".join(reversed(l)) #cba