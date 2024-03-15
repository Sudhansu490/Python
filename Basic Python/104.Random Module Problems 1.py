import random as r

# Q.1 Calculate the length
# l=[10,20,30,40,50,650]
# data=r.sample(l,k=True+True*2)
# print(len(data))  

# Q.2 Output=20(Yes/No)
# data=r.uniform(10,20)
# print(data)

# Q.3 Guess the number
# rn=r.randint(1,10)
# count=0
# while True:
#     count=count+1
#     choice=int(input('Guess a Number in between 1 to 10: '))
#     if choice==rn:
#         print('Congrats! Your guess number is correct.')
#         break
#     elif choice>rn:
#         print('Sry! Your guess number is greater than computer generated number.')
#     else:
#         print('Sry! Your guess number is less than computer generated number.')
# print(f'You have taken {count} steps to guess the Number.')

# one time password(4 digit password)
# otp=r.randint(0000,9999)
# print(otp)  # wrong
# print(r.randint(0,9),r.randint(0,9),r.randint(0,9),r.randint(0,9),sep='')

# generating 4 digit otp using loop
# otp=' '
# for i in range(4):
#     otp=otp+str(r.randint(0,9))
# print(otp)

# create 8 char password that must contain alphabets,digits & special symbols
# alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# digits='0123456789'
# special_symbols="!@#$%^&*_"
# print(r.choice(alpha),r.choice(alpha+digits),r.choice(special_symbols),r.choice(alpha),r.choice(digits),r.choice(special_symbols),r.choice(alpha),r.choice(special_symbols),sep='')