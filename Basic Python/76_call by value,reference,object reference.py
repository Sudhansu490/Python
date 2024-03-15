# call by value

# pass int(immutble object)
# def fun(a):
#     print('Inside function before modification: ',a)
#     print('Inside function before modification: ',id(a))
#     # modification on called function
#     a=1000
#     # here it will create a new object because int is immutable in nature
#     print('Inside function after modification: ',a)
#     print('Inside function after modification: ',id(a))

# a=23
# print('Outside function before calling: ',a)
# print('Outside function before calling: ',id(a))
# fun(a)
# print('Outside function after calling: ',a) # modification will not reflect to outside
# print('Outside function after calling: ',id(a)) 

# -------------------------------------------------------------------------------

# call by reference

# pass list(mutable object)
# def fun(l):
#     print('Inside function before modification: ',l)
#     print('Inside function before modification: ',id(l))
#     # modification on called function
#     l.append(40)
#     # here it will not create a new object because list is mutable in nature
#     print('Inside function after modification: ',l)
#     print('Inside function after modification: ',id(l))

# l=[10,20,30]
# print('Outside function before calling: ',l)
# print('Outside function before calling: ',id(l))
# fun(l)
# print('Outside function after calling: ',l) # modification will reflect to outside
# print('Outside function after calling: ',id(l)) 

# ---------------------------------------------------------------------------

# Conclusion => Python neither supports call by value nor call by reference.It supports call by object reference,it depends upon object.
# When we pass immutable object it behave likes call by value but when we pass mutable object it behave likes call by reference. 