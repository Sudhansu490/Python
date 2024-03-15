# def cal(a,b,c):
#     print(a+b*c)
# cal(5,6,7)  # 47(no problem)
# cal(6,7,5)  # 41(unexpected result->this is the issue)
# cal(b=6,c=7,a=5)  # 47(issues resolved->passing argument by using parameter name)

# positional argument & keyword argument
# cal(a=5,b=6,c=7)  # 47
# cal(5,6,c=7)
# cal(5,c=7,b=6)
# cal(5,a=6,b=7)  # TypeError: cal() got multiple values for argument 'a'
# cal(5,6,b=7)  # TypeError: cal() got multiple values for argument 'b'
# cal(5,b=6,7)  # SyntaxError: positional argument follows keyword argument
# cal(a=5,b,c)  # SyntaxError: positional argument follows keyword argument
# cal(a,c=6,b)  # SyntaxError: positional argument follows keyword argument

# cal(5,6,c=7)  # 47(issues resolved - that means we can't write keyword argument before positional argument)
# cal(5,b=6,c=7)

# ----------------------------------------------------------------------

# def cal(a,b,c,d,e,f):
#     print(a+b*c)
# cal(6,7,8,e=9,10,11)  # SyntaxError: positional argument follows keyword argument
# cal(6,7,f=8,10,11,a=9)  # SyntaxError: positional argument follows keyword argument

# -----------------------------------------------------------------------

# def cal(b,c,d,e,f,a):
#     print(a+b*c)
# cal(6,7,8,e=9,10,11)  # SyntaxError: positional argument follows keyword argument
# cal(6,7,10,11,a=9,f=8)  # 51