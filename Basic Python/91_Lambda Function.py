# Lambda Function(Anonymous Function)

# Addition of two number without using Lambda
# def add(a,b):
#     return a+b
# print(add(10,20))

# Addition of two number with using Lambda
# f=lambda a,b:a+b
# print(f(10,20))
# print(type(f))

# --------------------------------------------

# Square of a Number without using Lambda
# def sq(n):
#     return n*n
# print(sq(5))

# Square of a Number with using Lambda
# f=lambda a:a*a
# print(f(5))

# ---------------------------------------------------

# find out the greatest number among two without using Lambda
# def big(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(big(10,20))

# find out the greatest number among two using Lambda
# f=lambda a,b:a if a>b else b
# print(f(20,10))

# ------------------------------------------------

# Lambda return only 1 value(Only 1 expression it will return)
# f=lambda a,b:a,b  # NameError: name 'b' is not defined
# print(f(10,20))

# Lambda can return collections(list,tuple etc.)
# l=lambda a,b,c:[a,b,c]
# print(l(10,20,30))
# t=lambda a:(10,20,30,40,50)
# print(t(10,20))

# -----------------------------------------------------

# find out the greatest number among two using Lambda in one line
# print((lambda a,b:a if a>b else b)(10,12))

# ------------------------------------------------

# These are not the actual use of Lambda Function.
# Lambda Function is mainly used with higher order function filter(),map(),reduce() etc.
# Higher order Function means if a function takes another function as an argument.