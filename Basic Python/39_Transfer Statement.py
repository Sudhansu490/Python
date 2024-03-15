# break continue pass


# how to execute from the loop = break

# for i in range(10):
#     print(i)
#     if i==7:
#         break


# continue - skip
# 0 1 2 3 4  6 7  9

# for i in range(10):
#     if i==5 or i==8:
#         continue
#     print(i)

# for i in range(4):
#     print('Printing')
#     if i==2:
#         continue
#     print(i)

# pass - empty _Statement
# if you want to provide empty body then go for pass statement
# do nothing

# for i in range(10):
#     if i%2==0:
#         print(i)
#     else:
#         pass

for i in range(10):
    if i%2==0:
        pass
    else:
        print(i)