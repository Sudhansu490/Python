# using while loop

# n=int(input("Enter a Natural Number:"))
# sum=0
# if n<1:
#     print('Wrong Input! Take input again.')
# else:
#     while n>0:
#         sum+=n
#         n=n-1
#     print('The sum of n Natural Number is ',sum)


# using for loop

n=int(input("Enter a Natural Number:"))
sum=0
if n<1:
    print('Wrong Input! Take input again.')
else:
    for i in range(n+1):
        sum+=i
    print('The sum of n Natural Number is ',sum)