'''

heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공합니다.

힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한다.

힙 property : A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다

최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙



힙 함수 활용하기
heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
'''
import heapq


'''
heapq 모듈은 리스트를 최소 힙처럼 다룰 수 있도록 하기 때문에, 빈 리스트를 생성한 후 heapq의 함수를 호출할 때마다 리스트를  인자에 넘겨야 한다.

아래 코드는 heap이라는 빈 리스트를 생성하고 50, 10, 20을 각각 추가하는 예시이다.

'''


#원소 삽입
heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)

#원소 삭제
result = heapq.heappop(heap)

print(result)
print(heap)


#리스트 변환
heap2 = [50 ,10, 20]
heapq.heapify(heap2)

print(heap2)

#원소 접근

result2 = heap[0]

print(result2)
print(heap)


#최대 힙 만들기

'''
파이썬의 heapq 모듈은 최소 힙으로 구현되어 있기 때문에 최대 힙 구현을 위해서는 트릭이 필요하다.

IDEA: y = -x 변환을 하면 최솟값 정렬이 최댓값 정렬로 바뀐다.

힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다.  이때 원소 값의 부호를 바꿨기 때문에, 최소 힙으로 구현된 heapq 모듈을 최대 힙 구현에 활용하게 되는 것이다.

아래의 예시는 리스트 heap_items에 있는 원소들을 max_heap이라는 최대 힙 자료구조로 만드는 코드이다.

'''

heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

print(max_heap)

'''
그 결과 heappop을 사용하게 되면 힙에 있는 최댓값이 반환되는 것을 확인할 수 있다. 

이때 실제 원소 값은 튜플의 두 번째 자리에 저장되어 있으므로 [1] 인덱싱을 통해 접근하면 된다. 

'''


max_item = heapq.heappop(max_heap)[1]
print(max_item)