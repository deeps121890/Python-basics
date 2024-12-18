'''
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)  
'''
Output: [10, 20, 30, 40]
'''
my_list = [10, 20, 30]
my_list.remove(20)  # Removes the first occurrence of 20
print(my_list)  
'''
Output: [10, 30]
'''
my_list = [10, 20, 30]
popped_value = my_list.pop(1)  # Removes and returns item at index 1
print(popped_value) 
print(my_list)  

'''
 Output: 20
[10, 30]
'''
my_list = [30, 10, 20]
my_list.sort()  # Sorts the list in place
print(my_list)  
'''
Output: [10, 20, 30]
'''
my_list = [10, 20, 30]
my_list.reverse()
print(my_list)  
'''
Output: [30, 20, 10]



