'''

deque심층 정리

늘 bfs할 때 사용하는 deque 제대로 파악해보자.

데크(deque)의 개념
보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 반면, 양방향 큐가 있는데 그것이 바로 데크(deque)다.

즉, 앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.

데크는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.

컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 데크(deque)는 O(1)로 접근 가능하다.
'''

'''

데크(deque)에 존재하는 메서드(method)는 대략 다음과 같다.

deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
deque.remove(item): item을 데크에서 찾아 삭제한다.
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).



# Contain 1, 2, 3, 4, 5 in deq
deq = deque([1, 2, 3, 4, 5])

deq.rotate(1)
print(deq)
# deque([5, 1, 2, 3, 4])

deq.rotate(-1)
print(deq)
# deque([1, 2, 3, 4, 5])

이렇게 양수 값 또는 음수 값을 파라미터(parameter)로 제공하여 데크(deque)를 좌, 우로 회전할 수 있다.
'''



#1 Example 1: Appending Items Efficiently


# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

'''
deque:  deque([1, 2, 3])

The deque after appending at right is : 
deque([1, 2, 3, 4])

The deque after appending at left is : 
deque([6, 1, 2, 3, 4])

'''

#2 Example 2: Popping Items Efficiently

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([6, 1, 2, 3, 4])
print("deque: ", de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)


'''
deque:  deque([6, 1, 2, 3, 4])

The deque after deleting from right is : 
deque([6, 1, 2, 3])

The deque after deleting from left is : 
deque([1, 2, 3])

'''


# Example 3: Accessing Items in a deque

# index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
# insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
# remove():- This function removes the first occurrence of the value mentioned in arguments.
# count():- This function counts the number of occurrences of value mentioned in arguments.

# Python code to demonstrate working of
# insert(), index(), remove(), count()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5))

# using insert() to insert the value 3 at 5th position
de.insert(4,3)

# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print (de)

# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print (de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)

# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print (de)


'''

The number 4 first occurs at a position : 
4
The deque after inserting 3 at 5th position is : 
deque([1, 2, 3, 3, 3, 4, 2, 4])
The count of 3 in deque is : 
3
The deque after deleting first occurrence of 3 is : 
deque([1, 2, 3, 3, 4, 2, 4])

'''

#4 Example 4: Different operations on deque



# Python code to demonstrate working of
# extend(), extendleft(), rotate(), reverse()

# extend(iterable):- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
# extendleft(iterable):- This function is used to add multiple values at the left end of the deque. The argument passed is iterable. Order is reversed as a result of left appends.
# reverse():- This function is used to reverse the order of deque elements.
# rotate():- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3,])

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4,5,6])

# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to left end
de.extendleft([7,8,9])

# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print ("The deque after rotating deque is : ")
print (de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print ("The deque after reversing deque is : ")
print (de)

'''
The deque after extending deque at end is : 
deque([1, 2, 3, 4, 5, 6])
The deque after extending deque at beginning is : 
deque([9, 8, 7, 1, 2, 3, 4, 5, 6])
The deque after rotating deque is : 
deque([1, 2, 3, 4, 5, 6, 9, 8, 7])
The deque after reversing deque is : 
deque([7, 8, 9, 6, 5, 4, 3, 2, 1]) 


'''