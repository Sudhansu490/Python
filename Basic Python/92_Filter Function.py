# filter all the even value from a list without using Lambda
# def checkEven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l=[10,20,13,15,22,27]
# data=list(filter(checkEven,l))
# print(data)

# filter all the even value from a list with using Lambda
# l=[10,20,13,15,22,27]
# data=list(filter(lambda x:x%2==0,l))
# print(data)

# filter all the even value from a list with using Lambda in a single line.
# print(list(filter(lambda x:x%2==0,[10,20,13,15,22,27])))

# we can print also in the form of Tuple or Set.
# print(tuple(filter(lambda x:x%2==0,[10,20,13,15,22,27])))
# print(set(filter(lambda x:x%2==0,[10,20,13,15,22,27])))

# --------------------------------------------------------------

# filter all the negative numbers from a sequence(list,tuple,set etc.) using filter().
# s={10,-20,13,-15,-22,27}
# data=list(filter(lambda x:x<0,s))
# print(data)
# print(tuple(filter(lambda x:x<0,[10,-20,13,-15,-22,27])))

# filter all the positive numbers from a sequence(list,tuple,set etc.) using filter().
# s={10,-20,13,-15,-22,27}
# data=list(filter(lambda x:x>0,s))
# print(data)
# print(tuple(filter(lambda x:x>0,[10,-20,13,-15,-22,27])))

# ----------------------------------------------------------------------

# filter out all the common elements from both list using filter() function.
# l1=[10,20,30,40,50]
# l2=[5,20,25,30,50,100]
# data=list(filter(lambda x:x in l1,l2))
# print(data)

# --------------------------------------

# filter out a name 'kalyani' from a list using filter() function.
# names=['lipshika','prangya','kalyani','chinky']
# data1=tuple(filter(lambda x:x == 'kalyani',names))
# print(data1)
# data2=list(filter(lambda x:x != 'kalyani',names))
# print(data2)

# filter out all the even roll number students from the given dictionary.
# d={
#     1:'kalyani',
#     2:'lipshika',
#     3:'chinky',
#     4:'swastika',
#     5:'prangya',
#     6:'bijayini'
# }
# names=dict(filter(lambda x:x[0]%2==0,d.items()))
# print(names)