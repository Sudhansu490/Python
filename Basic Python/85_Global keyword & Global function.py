# Global Keyword

# If we want to define Global variable inside a function then we have to use Global keyword.
# def fun1():
#     global a
#     a=23  # Global Variable
#     print(a)
# def fun2():
#     print(a)
# fun1()
# fun2()

# By using Global Keyword we can perform modification operation on Global variable inside function.
# a=23
# def fun():
#     global a
#     a=99
#     print(a)
# fun()

# using same variable name we can't perform any operation berfore modification operation on the Global variable inside function.
# a=23
# def fun():
#     # print(a)  # SyntaxError: name 'a' is used prior to global declaration
#     global a
#     a=99
#     print(a)
# fun()

# But we can perform any operation using different variable name.
# a=23
# def fun():
#     b=999
#     print(b)
#     global a
#     a=99
#     print(a)
# fun()
# print(a)

# -----------------------------------------------------------------

# Global Function => globals()

# using globals() we can print the global variable inside a function after modification.
# a=23
# def fun():
#     a=999
#     print(a)  # 999
#     print(globals()['a'])  # 23
# fun()

# a=23
# def fun():
#     a=999
#     print(a)  # 999
#     data=globals()['a']  
#     print(data)  # 23
# fun()
# print(a)  # 23
# print(data)  # NameError(we can't print it outside the function.)