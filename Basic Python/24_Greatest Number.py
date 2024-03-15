#WAP to find the greatest of three numbers entered by the user.

a=int(input('Enter the value of a :'))
b=int(input('Enter the value of b :'))
c=int(input('Enter the value of c :'))


if a>b and a>c:
    print('a is the greatest Number')
elif b>c:
    print('b is the greatest Number')
else:
    print('c is the greatest Number')