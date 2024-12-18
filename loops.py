'''
x=1
while x<=10:
    print(x,end=' ')   
    x=x+1
print('end loop')
'''
o/p:1 2 3 4 5 6 7 8 9 10 end loop
'''
list=[1,2,3,4,5]
for i in list:
    print(i,end=",")
'''
o/p:1,2,3,4,5,
'''
tu=(1,2,3,4,5)
for i in tu:
    print(i)
'''
o/p: 1
2
3
4
5
'''
li=[10,20,30,40]
for i in range(0,len(li),2):
    print(li[i])
'''
O/P:
10
30
'''
st={1,2,3,4}
for i in st:
    print(i)
'''
o/p:1
2
3
4
'''
di={
    'x':121,
    'y':345}
for i in di:
    print(i,di[i])
'''
o/p:x 121
y 345






