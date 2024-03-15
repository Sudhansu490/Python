# 1.Tuple is immuuatable in nature.
# t=(10,20,30,40)
# t[1]=999
# print(t)

# 2.Tuple maintaining order.
# t=(10,20,30,40)
# print(t[2])

# 3.Tuple can hold different data items.
# t=(20,'sonu',True,20.40)
# print(t)

# 4.Duplicate elements are allowed.
# t=(10,20,30,40,10,20)
# print(t)

# 5.()parenthesis is optional but it is recommended.
# t=10,20,'sonu',False,20.40
# print(t)

# 6.Tuple support both positive and negative index.
# t=(10,20,30,40,50)
# print(t[2])
# print(t[-2])

# 7.Tuple packing &unpacking

# packing(individual to groups)
# a=23
# b=33
# c=50.35
# d='sonu'
# e=True
# t=a,b,c,d,e
# print(t)

# unpacking(groups to individuals)
# t=(23, 33, 50.35, 'sonu', True)
# a,b,c,d,e=t
# print(a,b,c,d,e)


# 8.Tuple returning multiple values
# def fun():
#     l=[10,20,30,40,50]
#     return(l[0],l[2],l[4])
# t=fun()
# print(t)
# print(type(t))
 

# 9.Tuple Comprehension is not possible in python.
# t=(i for i in range(10))
# print(t)   # <generator object <genexpr> at 0x0000017C5BC69A10>
# print(type(t))   # <class 'generator'>