'''
my_tuple = (10, 20, 30)  
print(my_tuple[1])  
'''
Output: 20
'''
my_tuple = (10, 20, 30, 40, 50)
print("Element at index 0:", my_tuple[0])  # Output: 10
print("Element at index 2:", my_tuple[2])  # Output: 30
'''
o/p:Element at index 0: 10
Element at index 2: 30
'''
my_tuple = (10, 20, 30, 20, 50, 20)
count_20 = my_tuple.count(20)
print("Occurrences of 20:", count_20)  
'''
Output: Occurrences of 20:3
'''
my_tuple = (10, 20, 30, 40, 50)
index_30 = my_tuple.index(30)
print("Index of 30:", index_30)
'''
Output:Index of 30: 2
