'''


결론적으로 파이썬에서는 "얕은 복사"냐 "깊은 복사"냐에 대해서 구분하고 학습해야 하는 객체는
int, float와 같은 immutable 한 객체들이 아니라 (X)
list, set, dictionary와 같은 mutable 한 객체들입니다. (O)

'''


## 얕은 복사



# ==

# mutable 한 객체 (리스트)
print('=' * 50)

arr1 = [1, 2, 3]
arr2 = arr1     # '=' 복사

print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

arr2.append(99)  # arr2 에 값 추가

print('\narr2.append(99)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')


# immutable 한 객체 (int)
print('=' * 50)

num1 = 30
num2 = num1     # 복사

print(f'num1 : {num1}, add : {hex(id(num1))}')
print(f'num2 : {num2}, add : {hex(id(num2))}')

num2 += 1
print('\nnum2 += 1')
print(f'num1 : {num1}, add : {hex(id(num1))}')
print(f'num2 : {num2}, add : {hex(id(num2))}')

'''

- mutable 한 객체인 리스트 예제
arr1, arr2를 '='을 통해서 복사를 하고 값과 주소를 보면 동일한 곳을 가리키고 있는걸 알 수 있습니다.
여기서 arr2.append(99)를 통해서 arr2에 값을 추가한 후에
arr1, arr2 를 둘 다 출력을 해보면
둘다 [1,2,3]에서 [1,2,3,99]로 값이 변경된 것을 알 수 있고, 참조하는 주소 또한 동일한 것을 알 수 있습니다.

이것이 참조만 복사하는 얕은 복사입니다. 

- immutable 한 객체 int 예제
int 타입을 복사하면 같은 참조를 가리키게 되고,
값을 변경했을 때 다른 주소를 가리키게 되는 것 을 볼 수 있습니다.
결국 각개 다른 참조.

'''


# [:]

print('=' * 50)

arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1[:]  # 여기서 복사

print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2 에 값 추가
print('arr2.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')


'''
1. 전체 출력
arr1을 [:] 리스트 슬라이싱을 통해서 arr2에 복사를 했습니다.
전체 출력 부분을 보면 보면 arr1과 arr2가 참조하는 메모리 주소가 다른 것을 볼 수 있습니다.
그래서 딱 봤을 때. "어? 메모리 주소 다르니까 깊은 복사 아니냐" 하실 수 있을 것 같습니다.

2. 리스트 끝에 값 추가
그래서 arr2.append(22)를 통해서 리스트 끝에 값을 추가해보았습니다.
그럼 arr1 = [4, 5, 6, [2, 4, 8]] 이 되고
arr2 = [4, 5, 6, [2, 4, 8], 22]로 리스트의 값이 다른 것을 볼 수 있네요.
이렇게만 보면 깊은 복사인 것 같은데.. 왜 얕은 복사라고 하는지 
궁금하시죠?

3. 리스트 내부 리스트
"리스트 안에 존재하는 리스트" 이 부분을 보면 확실히 얕은 복사인 게 느껴지실 것입니다.
arr1 [3] 부분이 [4, 5, 6, [2, 4, 8]]
arr2[3] = [4, 5, 6, [2, 4, 8], 22] 
바로 저 [2, 4, 8] 리스트인데요. 이 부분의 주소를 출력해보면
두 내부 리스트가 동일한 곳을 가리키고 있는 것을 볼 수 있습니다.
'아 이런 깊은 것 같았지만... 얕은 복사네요' 

4. 리스트 내부 리스트 값 추가
그럼 arr1[3] 부분이 정말 얕은 복사가 된 게 맞나 값을 추가해보았습니다.
arr1[3].append(99) 를 추가해서 출력해보니
arr1[3] 은 [2,4,8, 99]가 되었고
arr2[3] 또한 [2,4,8,99]가 된 것을 볼 수 있습니다. ' 야속한 얕은 복사 '이네요..

5. 전체 출력을 다시 한번 해보면
arr1 = [4, 5, 6, [2, 4, 8, 99]]
arr1 = [4, 5, 6, [2, 4, 8, 99], 22]
역시나 깊은 복사인 줄 알았던 [:] 슬라이싱이
내부적으로 보면 얕은 복사이었던 것을 알 수 있습니다.
겉에 있는 리스트만 새롭게 객체를 추가했지만 사실 내부에 있는 리스트 요소는 하나의 [2,4,8] 리스트를 가리키고 있던 것이었습니다.

완전한 깊은 복사도 아니고, 완전한 얕은 복사도 아니네요. 그렇지만 이것 또한 얕은 복사로 구분합니다.
'''



#copy 메서드

print('=' * 50)

arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1.copy()  # 여기서 복사 copy 메소드 이용

print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2 에 값 추가
print('arr2.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')


# import copy

import copy                 # copy 모듈 불러오기
print('=' * 50)

d1 = {'a': 'BlockDMask', 'b': [1, 2, 3]}
d2 = copy.copy(d1)      # copy 모듈 얕은복사

print("1. 전체 출력")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

print("\n2. 딕셔너리에 새 key, value 추가")
d2['c'] = 'kimchi'
print("d2['c'] = 'kimchi'")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

# 딕셔너리 내부에 리스트 value
print("\n3. 딕셔너리 내부 리스트")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n4. 딕셔너리 내부 리스트에 값 추가")
d1['b'].append('NO')
print("d1['b'].append('NO')")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n5. 딕셔너리 전체 다시 확인")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')


## 깊은 복사

'''
깊은 복사를 사용하기 위해서는 copy 모듈의 deepcopy 함수를 사용해야 합니다.

깊은 복사는 리스트 내부 리스트, 딕셔너리 내부 리스트 등 내부에 있는 객체 모두 새롭게 만들어주는 작업을 합니다.
모든 것 다 새롭게 복사. 그냥 독립적이 되어버림.

'''

import copy                 # copy 모듈 불러오기
print('=' * 50)

arr1 = [1, 2, [99, 88, 77], 3]
arr2 = copy.deepcopy(arr1)      # copy 모듈 깊은 복사

print("1. 전체 출력")
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')

print("\n2. 리스트에 새 key, value 추가")
arr1.append(0)
print('arr1.append(0)')
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')

# 리스트 내부에 리스트 추가
print("\n3. 리스트 내부 리스트.")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[2].append(10)
print("arr1[2].append(10)")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')


'''

1 번 전체 출력을 보면
arr1, arr2의 주소 값이 다른 것을 볼 수 있습니다.

3번의 리스트 내부 리스트도 보면 이전에 얕은 복사와 달리
arr1[2], arr2[2] 의 [99, 88, 77]인 리스트 내부 리스트도 주소 값이 다른 것을 볼 수 있습니다.

그래서 4번에서 리스트 내부 리스트인 arr1[2]에 값을 추가해도 arr2[2]에는 전혀 영향이 없는 것 을 알 수 있습니다.

즉, 복사한 이후부터는 '독립적이다.' '둘이 쌩깠다.' '이젠 아무 사이도 아니다.'인 상태가 "깊은 복사"인 것입니다.

 

'''