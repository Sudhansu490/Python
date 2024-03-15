a=int(input('Enter First Number :'))
b=int(input('Enter Second Number :'))

choice=input('Choices are- \n add \n sub \n mul \n div \n Enter a Choice:')

if choice=='add':
    print("Addition is ",a+b)
elif choice=='sub':
    print("Subtraction is ",a-b)
elif choice=='mul':
    print("Multiplication is ",a*b)
elif choice=='div':
    print("Division is ",a/b)
else:
    print("Invalid Option..!")