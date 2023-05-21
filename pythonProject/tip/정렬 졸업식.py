


# 버블 정렬

lst = [9,4,0,3,2,1,8]

def bubbleSort(lst):

    n = len(lst)

    #배열을 순회하면서, 모든 요소를 정렬 할 떄까지, 반복
    for i in range(n) :

        # 한 번의 순회 동안에 인접한 두 요소를 비교하면서, 큰 값을 뒤로 보낸다.
        for j in range(0, n - i - 1) :

            #현재 요소가 다음 요소보다 크면?! 두 요소를 교환
            if lst[j] > lst[j + 1] :

                lst[j], lst[j+1] = lst[j+1], lst[j]

# bubbleSort(lst)
#
# print(lst)

# 삽입 정렬

def insertionSort(lst) :

    n = len(lst)

    #배열을 모두 순회하면서 모든 요소를 정렬할 떄까지 반복
    for i in range(1, n) :
        key = lst[i]
        j = i - 1

        # key를 이미 정렬된 부분과 비교하면서, 적절한 위치에 삽입.
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            debug = 1
            j -= 1

        lst[j+1] = key

insertionSort(lst)

print(lst)

#퀵 정렬(quick sort)

def quick_sort(arr, low, high):
    if low < high:
        # 분할 작업을 수행하여 pivot을 올바른 위치로 이동합니다.
        pivot_index = partition(arr, low, high)

        # pivot을 기준으로 왼쪽과 오른쪽 부분 배열에 대해 재귀적으로 퀵 정렬을 수행합니다.
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    # pivot을 기준으로 작은 값과 큰 값으로 배열을 분할합니다.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def selection_sort(arr):
    n = len(arr)

    # 배열을 순회하면서 최소값을 찾아 앞으로 이동시킵니다.
    for i in range(n):
        min_index = i

        # 최소값을 탐색합니다.
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # 최소값을 현재 위치로 이동시킵니다.
        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort(arr):
    if len(arr) > 1:
        # 배열을 반으로 나눕니다.
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 왼쪽과 오른쪽 부분 배열에 대해 재귀적으로 병합 정렬을 수행합니다.
        merge_sort(left_half)
        merge_sort(right_half)

        # 정렬된 두 부분 배열을 병합합니다.
        merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    i = j = k = 0

    # 두 부분 배열을 비교하면서 정렬된 배열을 만듭니다.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # 남은 요소들을 복사합니다.
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 최대 힙 속성을 만족하도록 부모와 자식 노드를 비교하고 교환합니다.
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 초기 힙을 구성합니다.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 최대 힙에서 요소를 하나씩 추출하고 배열을 정렬합니다.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 각 숫자의 등장 횟수를 세기 위해 count 배열을 초기화합니다.
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # count 배열을 누적합으로 업데이트합니다.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # output 배열에 정렬된 숫자를 채웁니다.
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # output 배열을 원래 배열에 복사합니다.
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # 가장 큰 숫자의 자릿수를 찾습니다.
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10