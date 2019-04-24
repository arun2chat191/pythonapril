# x=10+20j
# print(x)
# print(type(x))
# print(x.real)
# print(x.imag)
#
# s='''classes by 'Durga' for "python" are very good'''
# print(s)

# s='durgasoftwaresolutions'
# output=s[0].upper() +s[1:len(s)-1]+ s[-1].upper()
# print(output)
# print(int(10.34))
# print(int(True))
# print(int(False))
# print(int('12'))
# print(float(0B1111))
# print(float(17))
# print(True)
# print(False)
# print(float("10"))
# print(float("durga"))
# print(complex(10)) #(10+0j)
# print(complex(0B1111)) #(15+0j)
# print(complex(15.0)) #(15+0j)
# print(complex(True))#(1+0j)
# print(complex(False))#0j
# print(complex("10.5"))
# print(complex(10,20))#(10+20j)
# print(complex(10.5,20.6))#(10.5+20.6j)
# print(bool(10))
# print(bool(0))
# print(bool(-1))
# print(bool(0.0000010))
# x=10
# print(id(x))
# x=x+1
# print(id(x))
# a=1000.234
# b=1000.234
# print(a is b)
l=[10,20,30]
# print(l)
# print(id (l))
# l[0]=3333
# print(l)
# print(id(l))
# l=[10,'durga',20,10,30]
# print(type(l))
# print(l)#orders preserved
# l=[]
# l.append(10)
# print(l)
# l.append(20)
# print(l)
# l.append(30)
# print(l)
# l.append(40)
# print(l)
# l.remove(40)
# print(l)
# l[1]=13
# print(l)

'''Tuples and list and dictionaries
examples'''

# t=(10,20,30,40,10,'durga')
# print(type(t))
# print(t[0])
# print(t[-1])
# print(t[1:4])
# t=(10,)
# print(type(t))
'''Tuples are immutable while lists are mutable,tuples takes less memory while list uses
more memory ,performance is higher in tuples while performance is lower in lists'''
# s={10,20,10,'durga',30,40}
# print(type(s))
# print(s)
#print(s[0])#does not support
#print(s[1:3])#does not support
# s.add(50)
# s.remove(30)
# print(s)
# s={}
# print(type(s))
#frozen set

# s={10,20,30,40}
# fr=frozenset(s)
# print(fr)

# d={100:'durga',200:'sunny',300:'chinny'}
# print(type(d))
# print(d)

# d={}
# d[100]='Durga'
# d[200]='Ravi'
# d[300]='sunny'
# print(d)
# d[100]='shiva'
# print(d)

# r=range(10)
# print(type(r))
# print(r)
# for x in r:
#     print(x)
# r=range(1,10)
# for x in r:
#     print(x)
# r=range(21,1,-3)
# for x in r:
#     print(x)
# r=range(1,21)
# print(r[0])
# print(r[-1])
# r=range(10,21)
# r1= r[1:5]
# for x in r1:
#     print(x)
# r[1]=1000

# l=[10,20,30,40,255]
# r=bytes(l)
# print(type(r))
# for x in r:
#     print(x)
#
# print(r[0])
# r[0]=77

l=[10,20,30,40]
b=bytearray(l)
# print(b[0])
# print(b[-1])
b[0]=77
for x in b:
    print(x)



