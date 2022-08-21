'''


1. product(iterator1, iterator2, .. , [repeat=1]) :

곱집합(cartesian product)

각 집합의 원소를 각 성분으로 하는 튜플들의 집합으로 데카르트 곱이라고도 함.

'''

from itertools import product, permutations, combinations, combinations_with_replacement
'''
데카르트 곱
'''

lst1 = [1, 2, 3]
lst2 = ["a", "b", "c"]

#1- 1 product를 사용
print(list(product(lst1, lst2)))

#1 - 2 이중포문으로 사용

lst = []

for i in lst1:
    for j in lst2:
        lst.append((i, j))
print(lst)

'''

중복 순열(순서 o, 중복 o)

'''

lst = ["a", "b", "c", "d", "e"]

print(list(product(lst, repeat = 1)))

print(list(product(lst, repeat = 2)))


'''

2. permutations(iterator, [len(iterator)]) : 순열(순서 o, 중복 x)

'''

iterator = ['A','B','C']

print(list(permutations(iterator))) #전체 배열 개수 만큼

print(list(permutations(iterator, 2))) #개수 지정

'''

3. combination(iterator, r) : 조합(순서 x, 중복 x)

'''

iterator = ['A','B','C']

print(list(combinations(iterator, len(iterator))))

print(list(combinations(iterator, 2)))


'''

4. combinations_with_replacement(iterator, r) : 중복조합 (순서 x, 중복 o)

중복 조합은 n개의 데이터 중에서 r개의 데이터를 뽑아 순서를 고려하지 않고
나열하는 모든 경우의 수이며 특히 데이터를 중복하여 뽑습니다.
중복 조합은 itertools 라이브러리에서 combinations_with_replacement 함수를 활용해 계산할 수 있습니다.

'''


iterator = ['A','B','C']
print(list(combinations_with_replacement(iterator, len(iterator))))
print(list(combinations_with_replacement(iterator, 2)),  "여기")