'''
x=10
def func():
    x=40
    y=20
    print(x)
    print(globals()['x'])
    print(globals()['y'])
func()
'''
o/p
40
10
