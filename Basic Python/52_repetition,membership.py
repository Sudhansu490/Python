# Repetition

# l = [10,20,30,40,50]
# r = l*3
# print(r)

# l = [10,20,30,40,50]
# r = l*l
# print(r)   # TypeError: can't multiply sequence by non-int of type 'list'

# l = [10,20,30,40,50]
# r = l*5.5
# print(r)   # TypeError: can't multiply sequence by non-int of type 'float'


# membership(in, not in)

# l=[10,20,30,40,50]
# print(20 in l)
# print(20 not in l)
# print(999 in l)
# print(999 not in l)


# Wap to check your lucky number is present inside list or not

# l=[1,3,4,5,7,8,9,11,15,16,18,19,22,25,27,29,31]
# choice=int(input('Enter your Lucky Number:'))
# if choice in l:
#     print('Yes. Your Lucky number is present inside the list.')
# else:
#     print('Sry, Your Lucky number is not present inside the list.')


# Wap to check your lucky number until match your lucky number with list element

# l=[1,3,4,5,7,8,9,11,15,16,18,19,22,25,27,29,31]
# choice=int(input('Enter your Lucky Number :'))
# while True:
#     if choice in l:
#         print('Yes,Your lucky Number is Present.')
#         break
#     else:
#         print('Sry,Your lucky Number is not present')
#         choice = int(input('Enter Your lucky Number again :'))