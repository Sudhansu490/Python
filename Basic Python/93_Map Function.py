# Add 4 to each & every element present in list without using Lambda
# create the body part for add4 function
# def add4(x):
#     return x+4
# l=[10,20,30,40,50]
# data=list(map(add4,l))
# print(data)

# Add 4 to each & every element present in list with using Lambda
# l=[10,20,30,40,50]
# data=list(map(lambda x:x+4,l))
# print(data)

# find out square of each number present inside tuple
# t=(1,2,3,4,5)
# data=list(map(lambda x:x*x,t))
# print(data)

# addition of list elements
# l1=[10,20,30,40,50]
# l2=[11,12,13,14,15]
# l3=[1,2,3,4,5]
# data=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
# print(data)

# find the length of each words present in a list
# names=['ananya','swastika','swagatika','saina']
# data=list(map(lambda x:len(x),names))
# print(data)
# for i in data:
#     print(i)

# find the length of each words present in a string
msg='Hello Guys I am Samrat'
data=list(map(lambda x:len(x),msg.split()))
print(data)