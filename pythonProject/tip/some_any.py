'''

any -> 하나라도 True면 True
all -> 전부 True여야 True
not any -> 전부 False여야 True
not all -> 하나라도 False면 True


'''

nums1 = [1,2,3,4,5,6,7]

n = 3

print(all(n < i for i in nums1)) #False
print(any(n < i for i in nums1)) #True

nums2 = [2,2,2,2]
n = 2
print(all(n == i for i in nums2)) #True
print(any(n != i for i in nums2)) #False