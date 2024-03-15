# 1.Direct Recursion
# def fun(num):
#     if num==6:
#         return
#     else:
#         print(num)
#         return fun(num+1)
# fun(1)

# ------------------------------

# 2.Indirect Recursion
# def fun1(n):
#     if n <= 6:
#         print(f'fun1 = {n*2}')
#         fun2(n+1)
#     return
# def fun2(n):
#     if n <= 6:
#         print(f'fun2 = {n*100}')
#         fun1(n+1)
#     return
# fun1(1)

# ------------------------------

# 3.Tail Recursion
# def fun(num):
#     if num==6:
#         return
#     else:
#         print(num)
#         fun(num+1)
# fun(1)

# ----------------------------------

# 4.Non-Tail Recursion
def fun(num):
    if num==6:
        return
    else:
        fun(num+1) # Recursive call
        print(num)
fun(1)