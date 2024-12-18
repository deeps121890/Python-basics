'''
my_dict = {'name': 'Alice', 'age': 25} 
print(my_dict['name'])
'''
o/p:
Alice
'''
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.get('name'))  
print(my_dict.get('location', 'Unknown'))  
'''
Output: Alice
Unknown (default value)
'''
my_dict = {'name': 'Alice', 'age': 25}
my_dict['location'] = 'New York'  # Adds a new key-value pair
my_dict['age'] = 26  # Updates the value for 'age'
print(my_dict)  
'''
Output: {'name': 'Alice', 'age': 26, 'location': 'New York'}
'''
my_dict = {'name': 'Alice', 'age': 25}
keys = my_dict.keys()
print(keys) 
values = my_dict.values()
print(values) 
'''
Output: dict_keys(['name', 'age'])
dict_values(['Alice', 25])

