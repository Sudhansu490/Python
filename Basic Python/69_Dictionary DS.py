# Duplicate keys are not allowed,if we write then it will update the value.
# d={
#     'name':'Sudhansu Nayak',
#     'name':'S R Nayak',
#     'Ph No':7205439529,
#     'address':'Bhubaneswar'
# }
# print(d)

# Dictionary keys are case sensitive.
# d={
#     'name':'Sudhansu Nayak',
#     'Name':'S R Nayak',
#     'Ph No':7205439529,
#     'address':'Bhubaneswar'
# }
# print(d)

# --------------------------------

# creations of Dictionary in different way

# 1.creation of empty dictionary:
# d={}
# print(d)
# print(type(d))

# 2.creation of empty dictionary using dict():
# d=dict()
# print(d)
# print(type(d))

# 3.create an empty dictionary then add items:
# d={}
# print(d)
# d[23]='sonu'
# d[24]='rahul'
# d[25]='silu'
# d[26]='anu'
# print(d)

# 4.creation of dictionary directly:
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d)

# -------------------------------------

# accessing the data of a dictionary
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d[24])
# print(d[30])   # KeyError: 30

# ---------------------------------------

# check a specified key is exists or not
 
# by using has_key() method -> it is available in python 2 version only
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.has_key(23))  # AttributeError

# using 'in' or 'not in' operator
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(23 in d)
# print(25 not in d)

# -------------------------------------------------

# create a dictionary dynamically by taking user input
# d={}
# while True:
#     key=input('Enter the key:')
#     val=input('Enter the value:')
#     d[key]=val
#     choice=input('Do you want to add more items[Y/N]:').upper()
#     if choice=='N':
#         break
# print(d)

# ----------------------------------------------------

# Traversing list
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# for i in d:
#     print(i, d[i])
#     # print(f'{i} --> {d[i]}')

# ------------------------------------------------------

# modification of dictionary(add,update,delete etc.)

# add
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d[27]='new'
# print(d)

# update
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d[24]='sweta'
# print(d)
# d[1024]='new'  # this key is not present in the dictionary then it will add this element in dictionary
# print(d)

# delete item
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# del d[25]
# print(d)
# del d[999]   # KeyError

# delete all items from the dictionary
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d.clear()   
# print(d)

# delete the dictionary
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# del d
# print(d)   # NameError: name 'd' is not defined.

# ---------------------------------------------------------

# Dictionary keys are always immutable in nature that means we can't change it.Hence we can't use list,set,dict as Dictionary key as they all are mutable in nature, but we can use Numbers,Tuple,Frozenset,float,bool,String as Dictionary key,otherwise we will get TypeError.

# d={[21,22,23]:'sonu',24:'rahul',25:'silu',26:'lipsa'}  # list
# print(d)  # TypeError: unhashable type: 'list'

# s=set(21,22,23)  # set
# d={s:'sonu',24:'rahul',25:'silu',26:'lipsa'} 
# print(d)  # Error

# d={{1:'one'}:'sonu',24:'rahul',25:'silu',26:'lipsa'}  # dictionary
# print(d)  # TypeError: unhashable type: 'dict'

# d={(21,22,23):'sonu',24:'rahul',25:'silu',26:'lipsa'}  # Tuple
# print(d) 

# fs=frozenset([21,22,23])  # frozenset
# d={fs:'sonu',24:'rahul',25:'silu',26:'lipsa'} 
# print(d)