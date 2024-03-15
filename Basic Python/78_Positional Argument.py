# positional argument means at the time of function calling we'll pass the arguments in correct positional order,otherwise we may get unexcepted result.
# def cal(a,b,c):
#     print(a+b*c)
# cal(10,15,20)  # 310(this is our expected result)
# cal(15,20,10)  # 215(unexpected result)
# cal(20,15,10)  # 170(unexpected result)

# The number of positional argument & parameter must be same.
# def fun(a,b,c):
#     print(a,b,c)
# fun([],(),{})
# fun(4,5,6)
# fun(5,6)  # TypeError: fun() missing 1 required positional argument: 'c'
# fun(5)  # TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
# fun([10,20,30])  # TypeError: fun() missing 2 required positional arguments: 'b' and 'c'

def fun():
    print('Hello Python! You are the best.')
fun()
# fun(10)  # TypeError: fun() takes 0 positional arguments but 1 was given
# fun(None)  # TypeError: fun() takes 0 positional arguments but 1 was given
# fun(())  # TypeError: fun() takes 0 positional arguments but 1 was given