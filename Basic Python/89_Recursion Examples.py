# print Number from 1 to 5 using Recursion
# def fun(num):
#     print(num)
#     if num==5:
#         return
#     fun(num+1)
# fun(1)

# def fun(num):
#     if num==3:
#         return
#     else:
#         fun(num+1)
#         print(num)
# fun(1)

# sum of n Natural Number
# def sum(n):
#     if n==1:
#         return n
#     return n+sum(n-1)
# print(sum(5))

# Factorial of a Number
# def fact(num):
#     if num==1:
#         return num
#     return num*fact(num-1)
# print(fact(4))

# Fibonacci Series(Each Number is equal to the sum of the previous 2 Numbers.)
# 0 1 1 => 2
# 0 1 1 2 => 3
# 0 1 1 2 3 => 5
# 0 1 1 2 3 5 => 8
# def fib(num):
#     if num<=1:
#         return num
#     else:
#         return fib(num-1)+fib(num-2)
# print(fib(3))

# ----------------------------------------

# Star Patterns

# def star(num):
#     print("* "*num)
#     if num==5:
#         return
#     star(num+1)
# star(1)

def star(num):
    print("* "*num)
    if num==1:
        return
    star(num-1)
star(5)