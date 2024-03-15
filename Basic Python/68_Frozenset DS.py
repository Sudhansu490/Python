# s={23,33,43,53,63}
# fs=frozenset(s)
# print(fs)
# print(type(fs))

# creating frozenset from list
# l=[23,33,43,53,63]
# fs=frozenset(l)
# print(fs)
# print(type(fs))

# fs=frozenset(range(11))
# print(fs)

# frozenset is immutable in nature so we can't use add(),remove() kind of methods.
# s={23,33,43,53,63}
# fs=frozenset(s)
# fs.add(73)   # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(23)   # AttributeError: 'frozenset' object has no attribute 'remove'

# applying other normal method which will not modify frozenset
# fs1=frozenset([23,33,43,53,63])
# fs2=frozenset([11,12,13,23,53])
# fs3=frozenset([23,43])
# fs4=frozenset([99,100])

# fs5=fs1.copy()
# print(fs5)
# print(fs1.union(fs2))
# print(fs1.intersection(fs3))
# print(fs1.difference(fs3))
# print(fs1.symmetric_difference(fs2))
# print(fs3.issubset(fs1))
# print(fs1.issuperset(fs4))
# print(fs3.isdisjoint(fs1))
# print(fs2.isdisjoint(fs4))