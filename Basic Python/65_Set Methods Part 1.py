# 1.add() -> used to add single element
# s={23,33,43,53,63}
# s.add(73)
# print(s)

# s={23,33,43,53,63}
# s.add(53)
# print(s)   # no effect

# s={23,33,43,53}
# s.add(63,73)
# print(s)  # TypeError: set.add() takes exactly one argument

# ---------------------------------------------------------------------------------

# 2.update() ->used to add multiple iterable elements(such as list,Tuple,range etc.)
# s={23,33,43,53}
# s.update(63,73)
# print(s)   # TypeError: 'int' object is not iterable

# s={23,33,43,53}
# l=[10,True,'sonu',55.23]
# t=(23.83,85,'Munu',False)
# s.update(l,t)
# print(s)

# s={23,33,43,53}
# l=[10,True,'sonu',55.23]
# t=(23.83,85,'Munu',False)
# s.update(l,t,range(99,105))
# print(s)

# --------------------------------------------------------------

# 3.remove() -> used to remove the specified element from the set
# s={23,33,43,53,63}
# s.remove(53)
# print(s)

# s={23,33,43,53,63}
# s.remove(73)
# print(s)   # KeyError: 73

# ---------------------------------------------------------

# 4.discard() -> exactly same as remove() but if the specified element is not present then it would not raise any KeyError.
# s={23,33,43,53,63}
# s.discard(53)
# print(s)

# s={23,33,43,53,63}
# s.discard(73)
# print(s)   # No effect

# -----------------------------------------------------------

# 5.pop() -> used to remove any random element from the set,if set is empty it will raised a KeyError
# s={23,33,43,53,63}
# s.pop()
# print(s)
# print(s.pop())

# s=set()
# s.pop()
# print(s)
# print(s.pop())   # KeyError: 'pop from an empty set'

# -------------------------------------------------------

# 6.copy() -> used to return a shallow copy of a set.

# shallow copy -> points to different memory location.
# s1={23,33,43,53,63}
# s2=s1.copy()
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))
# s1.add(999)
# print(s1)
# print(s2)

# deep copy -> points to same memory location.
# s1={23,33,43,53,63}
# s2=s1
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))
# s1.add(999)
# print(s1)
# print(s2)

# -------------------------------------------------------

# 7.clear() -> remove all the elements from the set.
# s={23,33,43,53,63}
# s.clear()
# print(s)

# -----------------------------------------------------------------

# 8.enumerate() -> return an enumerate object which contain index as well as value of all the items.
# s={23,33,43,53,63}
# for i in enumerate(s):
#     print(i)

# s={23,33,43,53,63}
# for i,j in enumerate(s):
#     print(i,' ',j)

# -------------------------------------------------------

# 9.max(),min() & sum()
# s={23,33,43,53,63}
# print(max(s))
# print(min(s))
# print(sum(s))

# ----------------------------------

# 10.sorted() -> sorted all the items of a set in ascending or descending order but in a list format.
# s={83,5,3,43,23,13}
# print(sorted(s))
# print(sorted(s,reverse=True))