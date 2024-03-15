# function returning another function

# This is the way we call Inner Function outside of Outer function.
# def outer():
#     print('I am inside outer.')
#     def inner():
#         print('I am inside inner.')
#     print('------------------')
#     return inner
# x=outer()
# x()  # Here we call Inner Function by using x

# def outer(abc):
#     return abc
# def inner():
#     print('Hello Python.')
# x=outer(inner)
# x()

# abc,x & data all are points to same memory location.
def fun1(abc):
    print(id(abc))
    return abc
def x():
    print(id(x))
    print('Python...')
data=fun1(x)
data()
print(id(data))