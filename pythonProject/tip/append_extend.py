#append


list = [2, 9, 3]

list.append('a')
print(list)

list.append([1, 2, 3])
print(list)


#extend

list = [2, 9, 3]
list2 = [1, 2, 3]
list.extend(list2)
print(list)

tuple = (4, 5, 6)
list.extend(tuple)
print(list)

#insert

list = [2, 9, 3]

list.insert(0, 'a')
print(list)

list.insert(2, 'b')
print(list)
