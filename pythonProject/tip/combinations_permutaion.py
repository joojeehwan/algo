'''

순열
permutation

순열이란 몇 개를 골라 순서를 고려해 나열한 경우의 수를 말한다. 즉, 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열하는 가짓수이며 순열이라는 의미의 영어 ‘Permutation’의 첫 글자 P를 따서 nPr로 표시한다. 출처 : [네이버 지식백과] 순열 [Permutation, 順列] (두산백과)

순열은 순서를 고려하기 때문에 [A, B, C]의 리스트에서 2개의 원소를 골라 순서를 정해 나열하면
[(A, B), (A, C), (B, A), (B, C), (C, A), (C, B)] 가 나오게 된다. 즉 순열에서는 (A, B)와 (B, A)는 다른 것이다.


'''

import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

'''

조합
combination
조합이란 서로 다른 n개 중에서 r개(n≥r) 취하여 조를 만들 때, 이 하나하나의 조를 n개 중에서 r개 취한 조합이라고 한다. 출처 : [네이버 지식백과] 조합 (두산백과)

조합은 순서를 고려하지 않기 때문에 [A, B, C]의 리스트에서 2개의 원소를 골라 나열하면
[(A, B), (A, C), (B, C)] 가 나오게 된다. 조합은 (A, B)와 (B, A)는 같은 것으로 취급한다.

'''

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

#결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]