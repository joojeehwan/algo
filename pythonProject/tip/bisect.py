from bisect import bisect_right, bisect_left

lst = [1, 4, 6, 10]

print(bisect_left(lst, 6))  # result = 2
print(bisect_right(lst, 6))  # result = 3


'''
1.
해당 값이 리스트에 있을 때

bisect_left - 해당 index 반환

bisect_right - 해당 index + 1 반환

'''

print(bisect_left(lst, 9))  # result = 3
print(bisect_right(lst, 9))  # result = 3


'''
2.해당 값이 리스트에 없을 때

bisect_left - 리스트 오름차순에 들어갈 index 반환

bisect_right - 리스트 오름차순에 들어갈 index 반환

'''

'''

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 의 정렬된 배열이 있을 때,
현재 정렬된 상태를 유지하면서 n = 5 이라는 요소를 배열에 추가하고 싶다고 해봅시다.
어떤 인덱스에 넣어야하는지 계산하는 함수를 구해봅시다.

'''

#이분탐색x vs 이분탐색
nums = [0,1,2,3,4,5,6,7,8,9]
n = 5
for i in range(len(nums)):
    if n <= nums[i]:
        break
result = i
print(result)

'''
결과값
5
'''


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 5
l = 0
r = len(nums) - 1
result = 0
while l <= r:
    mid = (l + r) // 2
    if nums[mid] >= n:
        result = mid
        r = mid - 1
    else:
        l = mid + 1

print(result)

'''
결과값
5
'''

from bisect import bisect_left, bisect_right

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))

'''
결과값
5
6
'''

