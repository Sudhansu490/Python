# how to print description about a function?
# print(fun_name.__doc__)
# print(len.__doc__)
# print(type.__doc__)

# def keyword is used to define user defined function.

# def add(a,b,c):
#     '''this function is used to perform addition of three numbers''' 
#     print(a+b+c)
# add(10,20,30)
# add(11,12,13)
# print(add.__doc__)

# when we take same variable name then both parameter & argument are points to same memory location.
# def add(a,b,c):
#     print('Inside Function')
#     print(id(a))
#     print(id(b))
#     print(id(c))
#     print(a,b,c)
# a,b,c=10,20,30    
# add(a,b,c)
# print('Outside Function')
# print(id(a))
# print(id(b))
# print(id(c))
# print(a,b,c)

# when we take different variable name then also both parameter & argument points to same memory location
# def add(x,y,z):
#     print('Inside Function')
#     print(id(x))
#     print(id(y))
#     print(id(z))
#     print(x,y,z)
# a,b,c=10,20,30    
# add(a,b,c)
# print('Outside Function')
# print(id(a))
# print(id(b))
# print(id(c))
# print(a,b,c)

# when we take different variable name but we update the value then both parameter & argument are points to different memory location after modification.
def add(x,y,z):
    print('Inside Function')
    x=1000
    print(id(x))
    print(id(y))
    print(id(z))
    print(x,y,z)
a,b,c=10,20,30    
add(a,b,c)
print('Outside Function')
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)