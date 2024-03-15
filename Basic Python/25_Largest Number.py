# WAP to find largest among four numbers entered by the user.


num1=int(input('Enter 1st Number:'))
num2=int(input('Enter 2nd Number:')) 
num3=int(input('Enter 3rd Number:')) 
num4=int(input('Enter 4th Number:')) 

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print(str(f1) + " is the Largest Number.")
else:
    print(str(f2) + " is the Largest Number.")