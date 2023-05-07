target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0
right = length-1

while left<=right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1


#이분탐색 공부 10.19

def binarySearch(array, target, left, right):
    middle_idx = (left+right)//2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        print('answer {}'.format(middle_idx))
    elif middle > target:
        binarySearch(array, target,left,middle_idx-1)
    elif middle < target:
        binarySearch(array, target,middle_idx+1,right)
    else:
        return False

target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0
right = length-1

binarySearch(m_list,target,0,right)


# 이분탐색의 응용 Lower bound / upper bound

'''
정렬된 리스트에서 k가 들어갈 적절한 위치를 찾고 싶습니다.
단, 리스트에는 k가 존재할 수도 있고 없을 수도 있습니다.
따라서 이 경우, 이진탐색(=정렬된 데이터에서 k를 정확하게 찾는 알고리즘)을 조금 변형한 lower bound 또는 upper bound 알고리즘을 사용해야 합니다.


Lower Bound
k '이상'이 처음 나오는 위치입니다.

Upper Bound
k를 '초과'한 값이 처음 나오는 위치입니다.

예시
다음과 같은 정렬된 리스트가 있습니다. k = 4 입니다.

값	        0	1	2	4	4	4	7	8
위치(index)	0	1	2	3	4	5	6	7

ⓐ lower bound?
k(=4) 이상의 값이 처음 나오는 위치를 찾습니다.
lower bound는 index = 3 입니다.

ⓑ upper bound?
k(=4) 초과의 값이 처음 나오는 위치를 찾습니다.
upper bound는 index = 6 입니다.


참고로...
파이썬에는 bisect라는 라이브러리가 존재합니다.
bisect_left(iterable, k) : lower bound와 동일합니다.
bisect_right(iterable, k) : upper bound와 동일합니다.

'''

def lowerbound(array, k):
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

		# 📢 이 부분 주의!
        if array[mid] >= k:
            right = mid
        else:
            left = mid + 1

    return left


def upperbound(array, k):
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

        # 📢 이 부분 주의!
        if array[mid] <= k:
            left = mid + 1
        else:
            right = mid

    return left