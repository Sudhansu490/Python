# 1.get() -> used to return the corresponding value associated with that key.
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.get(23))
# print(d.get(99))  # None
# print(d.get(99,'unknown'))  # unknown

# difference between d[Key] & get(Key) method
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.get(99))  # None
# print(d[99])  # KeyError

# -------------------------------------------------

# 2.items() -> used to return list of Tuple that contain key and value as a pair.
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.items())
# for i in d.items():
#     print(i)
# for i,j in d.items():
#     print(i,j)

# ---------------------------------------------

# 3.pop() -> used to remove the Key with its associated value,then it will return that value.
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.pop(23))
# print(d.pop(99))  # KeyError
# print(d.pop())   # TypeError: pop expected at least 1 argument, got 0

# ----------------------------------------------------------------

# 4.popitem() -> used to remove the last inserted item in dictionary & return that item in Tuple format.
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.popitem())
# print(d)

# if dictionary is empty then it will raise a KeyError.
# d={}
# print(d.popitem())  # KeyError: 'popitem(): dictionary is empty'

# --------------------------------------------------------------------

# 5.keys() -> used to return alll the keys of dictionary in list format.
# 6.values() -> used to return all the values of dictionary in list format.
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.keys())
# print(d.values())
# for i in d.keys():
#     print(i)
# for j in d.values():
#     print(j)

# -----------------------------------------

# 7.setdefault() -> used to return the value associated with that specified key. If the key is not available  then key & value will be added as new item to the dictionary.
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# print(d.setdefault(25))   # silu
# print(d.setdefault(27,'anjali'))  # it added into the dictionary
# print(d)
# print(d.setdefault(23,'Puja'))   # it ignores 'Puja' & returns 'sonu' as key:23 is available.
# print(d.setdefault(99))  # None(if we will not provide any value then it will return 'None' by default.)
# print(d)

# -----------------------------------------------------------------

# 8.update() -> used to add all the items from a dictionary to another dictionary
# d1={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d2={1:'school',2:'college',3:'university'}
# d1.update(d2)
# print(d1)
# print(d2)

# if the key of both dictionary is same then it will be consider the updated one.
# d1={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d2={23:'school',24:'college',25:'university'}
# d1.update(d2)  # d1 will be updated.
# print(d1)
# print(d2)

# ------------------------------------------------------------------

# 9.copy() -> used to return a shallow copy of a dictionary.

# shallow copy -> points to different memory location.
# d1={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d2=d1.copy()
# print(d1)
# print(d2)
# print(id(d1))
# print(id(d2))
# d1[99]='new'
# print(d1)
# print(d2)

# deep copy -> points to same memory location.
# d1={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d2=d1
# print(d1)
# print(d2)
# print(id(d1))
# print(id(d2))
# d1[99]='new'
# print(d1)
# print(d2)

# ------------------------------------------------

# 10.clear() -> used to remove all items from the dictionary.
# d={23:'sonu',24:'rahul',25:'silu',26:'lipsa'}
# d.clear()
# print(d)

# -----------------------------------------------------------------------------------

# 11.fromkeys() -> used to create a new dictionary from given iterable(list,Tuple,range etc.) object and value(optional).

# create a dictionary from list
# l=[23,33,43,53,63]
# d=dict.fromkeys(l)
# print(d)

# create a dictionary from Tuple
# t=(23,33,43,53,63)
# d=dict.fromkeys(t)
# print(d)

# create a dictionary from range()
# r=range(5)
# d=dict.fromkeys(r)
# print(d)

# create a dictionary from range() along with value
# r=range(5)
# d=dict.fromkeys(r,'ananya')
# print(d)

# if we provide the iterrable object then what will be the o/p?
# l=[1,2,3]
# d=dict.fromkeys(l,l)
# print(d)

# r=range(5)
# l=[]
# d=dict.fromkeys(r,l)
# print(d)

# l=[]
# d=dict.fromkeys(l,l)
# print(d)