'''

case 1. 더 넓은 범위에 있는 변수 '읽기'는 가능
아래와 같이 전역변수로 n을 선언하고 이를 함수 내에서 읽기만 하는 경우 에러가 나지 않는다.


'''

n = 0
def func():
	print(n) # 0
func()


'''

아래와 같은 경우도 마찬가지이다. 전역 변수는 아니고 func2를 감싸고 있는 func1에서 설정한 변수지만 func2 내부에서 사용이 가능하다.

'''

def func1():
    n = 1
    def func2():
        print(n) # 1
    func2()
func1()


'''

case2. 더 넓은 범위에 있는 변수 '변경'은 불가능

'''

n = 0
def func():
    n += 1 # error
    print(n)
func()
def func1():
  n = 1
  def func2():
  	n += 1 # error
  	print(n)
  func2()
func1()


'''

global


n을 전역변수로 선언해주고 함수 내부에서 편집을 원할 때, 

'나는 지금 함수 내의 n이 아닌 전역변수 n을 쓸거야'라는 의미로 global n이라고 선언해주면 문제없이 사용이 가능하다.
'''

n = 1
def func1():
  def func2():
    global n
    n += 1
    print(n) # 2
  func2()
func1()


'''

전역 변수가 아닌 경우

만약 위와 같이 전역 변수 n이 아닌 변수에 global 키워드로 지정해준다면 NameError: name 'n' is not defined에러가 발생한다.
이는 전역변수로 선언된 n이 없기 때문이다.
이런 경우는 global이 아닌 nonlocal 키워드를 사용해야한다.
 

'''


def func1():
  n = 1
  def func2():
    global n
    n += 1
    print(n) # error
  func2()
func1()


'''
nonlocal

아래와 같이 현재의 scope내의 지역변수가 아니고, 전역변수도 아닌 변수 n을 사용할 때는 nonlocal키워드를 써준다.
'나는 지금 지역변수는 아닌 변수를 사용할거야'라는 의미로 nonlocal n이라고 설정해주면 문제없이 사용 가능하다.
'''

def func1():
  n = 1
  def func2():
    nonlocal n
    n += 1
    print(n) # 2
  func2()
func1()