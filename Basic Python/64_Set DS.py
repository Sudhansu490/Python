# creations of set in different ways

# creation of empty set
# s={}
# print(s)
# print(type(s))  # <class 'dict'>

# 1.way of creating empty set
# s=set()
# print(s)
# print(type(s))

# 2.creation of set with multiple elements
# s={23,43,63,83}
# print(s)  # set doesn't maintain order

# 3.creation of set with heterogenous elements
# s={23,43.3,'sonu',True}
# print(s)

# 4.creation of set using set()

# creation of set using list
# l=[23,33,43,53]
# s=set(l)
# print(s)

# creation of set from Tuple
# t=(23,33,43,53)
# s=set(t)
# print(s)

# creation of set using range()
# s=set(range(10))
# print(s)
 
# creation of set from string
# name='Sudhansu Ranjan Nayak'
# s=set(name)
# print(s)

# name='Sudhansu Ranjan Nayak'
# s=set(name.split())
# print(s)

# s=set('Sudhansu Ranjan Nayak')
# print(s)

# --------------------------------

# we can't apply indexing and slicing concept
# s={23,33,43,53,63}
# print(s[2])   # TypeError: 'set' object is not subscriptable
# print(s[1::])  # TypeError: 'set' object is not subscriptable

# in & not in 
# s={23,43.3,'sonu',True}
# print('sonu' in s)
# print('munu' in s)
# print('52' not in s)
# print(True not in s)