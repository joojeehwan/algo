'''
모듈 임포트
우선 heapq 모듈은 내장 모듈이기 때문에 파이썬만 설치되어 있으면 다음과 같이 간단하게 임포트 후에 힙 관련 함수를 사용할 수 있습니다.
'''
import heapq

'''
최소 힙 생성
heapq 모듈에은 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와줍니다. 자바의 PriorityQueue 클래스처럼 리스트와 별개의 자료구조가 아닌 점에 유의해야 합니다.

그렇게 때문에, 그냥 빈 리스트를 생성해놓은 다음 heapq 모듈의 함수를 호출할 때 마다 이 리스트를 인자로 넘겨야 합니다. 다시말해, 파이썬에서는 heapq 모듈을 통해서 원소를 추가하거나 삭제한 리스트가 그냥 최소 힙입니다.

'''
heap = []

'''
힙에 원소 추가
heapq 모듈의 heappush() 함수를 이용하여 힙에 원소를 추가할 수 있습니다. 첫번째 인자는 원소를 추가할 대상 리스트이며 두번째 인자는 추가할 원소를 넘깁니다
'''
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
'''
힙에서 원소 삭제
가장 작은 1이 인덱스 0에 위치하며, 인덱스 1(= k)에 위치한 3은 인덱스 3(= 2k + 1)에 위치한 4보다 크므로 힙의 공식을 만족합니다. 내부적으로 이진 트리에 원소를 추가하는 heappush() 함수는 O(logN)의 시간 복잡도를 가집니다.
'''
print(heap)
'''
heapq 모듈의 heappop() 함수를 이용하여 힙에서 원소를 삭제할 수 있습니다. 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴합니다.

'''
print(heapq.heappop(heap))
print(heap)

'''
기존 리스트를 힙으로 변환
이미 원소가 들어있는 리스트 힙으로 만들려면 heapq 모듈의 heapify()라는 함수에 사용하면 됩니다.
heapify() 함수에 리스트를 인자로 넘기면 리스트 내부의 원소들의 위에서 다룬 힙 구조에 맞게 재배치되며 최소값이 0번째 인덱스에 위치됩니다. 
즉, 비어있는 리스트를 생성한 후 heappush() 함수로 원소를 하나씩 추가한 효과가 납니다. heapify() 함수의 성능은 인자로 넘기는 리스트의 원소수에 비례합니다. 즉 O(N)의 시간 복잡도를 가집니다.
'''

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)

'''
최소값 삭제하지 않고 얻기
힙에서 최소값을 삭제하지 않고 단순히 읽기만 하려면 일반적으로 리스트의 첫번째 원소에 접근하듯이 인덱스를 통해 접근하면 됩니다.

여기서 주의사항은 인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것입니다. 
왜냐하면 힙은 heappop() 함수를 호출하여 원소를 삭제할 때마다 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문입니다.
따라서 두번째로 작은 원소를 얻으려면 바로 heap[1]으로 접근하면 안되고, 반드시 heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]를 통해 새로운 최소값에 접근해야 합니다.
'''
print(heap[0])



#응용

#1. 최대힙
'''
heapq 모듈은 최소 힙(min heap)을 기능만을 동작하기 때문에 최대 힙(max heap)으로 활용하려면 약간의 요령이 필요합니다.
바로 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것입니다.
따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, (우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제하면 됩니다.
그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됩니다. (우선 순위에는 관심이 없으므로 )

'''

#2. k번쨰 최소값 / 최대값

import heapq

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

# 3.힙정렬

import heapq

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))