# 1.append() method

# l=[23,33,43,53,64]
# print(l)
# l.append(678)
# print(l)
# l.append(789)
# print(l)

# Create a list by adding 10 0's
# l=[]
# for i in range(10):
#     l.append(0)
# print(l)

# Create a list by adding 0 to 10 
# l=[]
# for i in range(11):
#     l.append(i)
# print(l)


# 2.insert() method

# l=[23,33,43,53,64]
# print(l)
# l.insert(2,999)
# print(l)

# l=[23,33,43,53,64]
# print(l)
# l.insert(20,999)
# print(l)

# l=[23,33,43,53,64]
# print(l)
# l.insert(-20,999)
# print(l)


# 3.count() method

# l=[23,33,23,43,53,23,63,33]
# print(l.count(23))
# print(l.count(888))


# 4.index() method

# l=[23,33,23,43,53,23,63,99]
# print(l.index(23))
# print(l.index(43))
# print(l.index(999))  # ValueError


# 5.remove() method

# l=[10,20,23,33,23,11,22,44,23]
# l.remove(23)
# print(l)
# l.remove(11)
# print(l)
# l.remove(999)  # ValueError


# 6.pop() method

# l=[23,33,43,52,63]
# print(l.pop())
# print(l)
# print(l.pop(2))
# print(l)
# print(l.pop(99))  # IndexError: pop index out of range


# 7.extends() method

# l=[10,20,30,40]
# s=[100,200,300,400,500]
# l.extend(s)
# print(l)


# 8.reverse() method

# l=[10,20,30,40,50]
# l.reverse()
# print(l)


# 9.sort() method

# l=[10,2,20,3,6,1,8]
# l.sort()
# print(l)

# l=[10,2,20,3,6,1,8]
# l.sort(reverse=True)
# print(l)

# l=['sonu','ananya','swagatika','lina']
# l.sort()
# print(l)

# l=['sudhansu','ananya','swagatika','lina',23,33,53]
# l.sort()
# print(l)  # TypeError: '<' not supported between instances of 'int' and 'str'


# 10.clear() method
# l=[10,20,30,40,50]
# print(l)
# l.clear()
# print(l)


# 11.copy() method

# l=[10,20,30,40,50]
# s=l.copy()  # cloning

# print(l)
# print(s)

# print(id(l))  
# print(id(s))

# s[2]=999
# print(l)
# print(s)


# assign 

# l=[10,20,30,40,50]
# s=l  # assigning

# print(l)
# print(s)

# print(id(l))  
# print(id(s))

# s[2]=999
# print(l)
# print(s)