# It is use to create a Dictionary from iterable objects like list,tuple,range by writing less number of code.

# d={i:i for i in range(1,6)}
# print(d)

# d={i:i*i for i in range(1,6)}
# print(d)

# working with list to create a Dictionary
# l=[7,14,21,28]
# d={r:3.14*r*r for r in l}
# print(d)

# names=['Sonu','Ananya','Prangya','Swastika']
# d={i:len(i) for i in names}
# print(d)

# names=['Sonu','Ananya','Prangya','Swastika']
# d={i:len(i) for i in names if len(i)>6}
# print(d)