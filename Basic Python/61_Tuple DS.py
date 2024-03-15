# creation of tuple in different way

# 1.Creation of empty tuple
# t=()
# print(t)
# print(type(t))

# 2.Creation of tuple with single value
t=(20,)
print(t)
print(type(t))

# 3.creation of tuple without using ()
# t=10,20,'sonu',False,20.40
# print(t)
# print(type(t))  # So () is optional but is highly recommended that you have to give that.

# 4.creation of tuple using tuple()
# l=[10,20,30,40]
# t=tuple(l)  # conversion from list to tuple
# print(l)
# print(t)
# t=tuple(range(10))
# print(t)
# t=tuple('sudhansu')
# print(t)

# ---------------------------------------------------------

# Accessing elements of Tuple

# 1.Accessing by Index
# t=(10,20,30,40,50)
# print(t[0])
# print(t[2])
# print(t[-2])
# print(t[50])  # IndexError: tuple index out of range

# 2.Accessing by Slice Operator
# t=(10,20,30,40,50)
# print(t[::])
# print(t[:2])
# print(t[::2])

# -----------------------------------------------------

# Perform basic mathematical operation on Tuple

# 1.Concatension operation(+)
# t1=(10,20,30,40,50)
# t2=(60,70,80,90)
# t3=(5,15,25,35,45)
# t = t1+t2+t3
# print(t)

# 2.Repitition Operation
# t=(23,33,43,53)
# l=t*3
# print(l)

# ---------------------------------------------------------

# Traversing operation on tuple

# 1.Traversing using for loop
# t=(10,20,30,40,50)
# for i in t:
#     print(i)

# 2.Traversing using while loop
# t=(10,20,30,40,50)
# i=0
# while i<len(t):
#     print(t[i])
#     i=i+1

# ----------------------------------------------------------

# Nested Tuple

# t=(23,'sonu',('munu',50,True),45.20)
# print(t[2][-1])
# for i in t:
#     print(i)

# t=(23,'sonu',['munu',50,True],45.20)
# t[2][-3]='anjali'
# for i in t:
#     print(i)