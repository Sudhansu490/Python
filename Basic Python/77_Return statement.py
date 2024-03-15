# without return statement
# def fun(a):
#     print(a)
# print(fun(10)) # None

# with return statement
# def fun(a):
#     print(a)
#     return a*a
# print(fun(10)) # 100

# def fun(a,b,c):
#     return a+b+c
# print(fun(10,20,30))

# return a list
# def fun():
#     l=[10,20,30]
#     return l
# x=fun()
# print(x)
# for i in x:
#     print(i)

# function returning multiple values
# def fun(a,b,c):
#     return a,b,c
# print(fun(10,20,30))

# if we'll write any statement after return statement then it will not execute those statements.
# def fun():
#     print('Good Morning')
#     print('Good Afternoon')
#     return 10
#     print('Good Evening')
#     print('Good Night')
# fun()

# define a function it will take 6 subjects mark of a student as an argument then return totalmark & avgmark

# using only 1 return statement
# def cal(p,c,m,e,o,i):
#     tm=p+c+m+e+o+i
#     print('Total mark is ',tm)
#     am=tm/6
#     return am
# print('Average mark is ',cal(80,79,89,74,84,92))

# using multiple return statements
def cal(p,c,m,e,o,i):
    tm=p+c+m+e+o+i
    am=tm/6
    return tm,am
tm,am=(cal(80,79,89,74,84,92))
print('Total mark is ',tm)
print('Average mark is ',am)