# def fun(a,b,c):
#     print(a+b*c)
# fun(10,20)  # TypeError: fun() missing 1 required positional argument: 'c'

# Default Argument
# def wishme(name='unknown'):
#     print(f'Hello {name}, Good Morning.')
# wishme('Lipsa')
# wishme()

# def wishme(bf,gf='You do not have any GF'):
#     print(f'Hello {bf},Your GF Name is {gf}')
# wishme('rahul','saina')
# wishme('Sonu')

# def wishme(bf='You do not have any BF',gf):
#     print(f'Hello {bf},Your GF Name is {gf}')
# wishme('rahul','saina')  # SyntaxError: non-default argument follows default argument

# def student(name,id,email='not available',mark):
#     print('Name is ',name)
#     print('ID is ',id)
#     print('Email is ',email)
#     print('Mark is ',mark)
# student('sonu',2001297198,90)  # SyntaxError: non-default argument follows default argument

# def student(name,id,mark,email='not available'):
#     print('Name is ',name)
#     print('ID is ',id)
#     print('Email is ',email)
#     print('Mark is ',mark)
# student('sonu',2001297198,90)

# def student(name,id,mark,email='not available',addr='not available'):
#     print('Name is ',name)
#     print('ID is ',id)
#     print('Email is ',email)  # BBSR
#     print('Mark is ',mark)
#     print('Address is ',addr)
# student('sonu',2001297198,90,'BBSR')  # wrong