'''
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  
'''
Output: {1, 2, 3, 4}
'''
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set) 
my_set.discard(10)  # Will not raise error, even though 10 is not in the set
print(my_set)
'''
Output: {1, 3}
'''
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set) 
'''
Output: {1, 2, 3, 4, 5}
'''
union_set = set_a | set_b
print(union_set)  
''' 
Output: {1, 2, 3, 4, 5}
'''
set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersection_set = set_a.intersection(set_b)
print(intersection_set)  
'''
 Output: {3}
'''
intersection_set = set_a & set_b
print(intersection_set)  
'''
Output: {3}
