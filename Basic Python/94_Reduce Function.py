# reduce function is not available here.We have to import this from functools module.
from functools import reduce

# find the sum of all elements present in a list without using Lambda.
# def sum(x,y):
#     return x+y
# l=[1,2,3,4,5]
# data=reduce(sum,l)
# print(data)

# find the sum of all elements present in a list with using Lambda.
# l=[1,2,3,4,5]
# data=reduce(lambda x,y:x+y,l)
# print(data)
# print(type(data))  # <class 'int'>

# find the product of all elements present in a list.
# l=[1,2,3,4,5]
# data=reduce(lambda x,y:x*y,l)
# print(data)

# find the sum of all elements from 1 to 100
# data=reduce(lambda x,y:x+y,range(1,101))
# print(data)

# works with string which presents in a list
# l=['ananya','swastika','saina','lipshika']
# data=reduce(lambda x,y:x+y,l)  # concatenation
# print(data)
# print(type(data))  # <class 'str'>

# working with Dictionary
# d={
#     1:'ananya',
#     2:'swastika',
#     3:'saina',
#     4:'lipshika'
# }
# data1=reduce(lambda x,y:x+y,d.keys())
# print(data1)
# data2=reduce(lambda x,y:x+y,d.values())
# print(data2)

# -------------------------------------------

# reduce vs accumulate
# accumulate function is not available here.We have to import this from itertools module.
from itertools import accumulate
l=[1,2,3,4,5]
print(list(accumulate(l,lambda x,y:x+y)))
print(reduce(lambda x,y:x+y,l))