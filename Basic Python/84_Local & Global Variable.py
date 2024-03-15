# Local Variable

# def fun():
#     a=23  # local variable
#     print(a)
# fun()
# print(a)  # NameError: name 'a' is not defined

# def fun1():
#     a=23  # local variable
#     print(a)
# def fun2():
#     print(a)
# fun1()
# fun2()  # NameError: name 'a' is not defined

# ---------------------------------------------

# Global Variable

# a=23  # Global variable
# def fun1():
#     print(a)
# def fun2():
#     print(a)
# fun1()
# fun2() 
# print(a)

# Local Variable is having more scope than Global Variable.
a=23  # Global Variable
def fun():
    a=999  # Local Variable
    print(a)
fun()