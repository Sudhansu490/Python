# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(0,num-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num,0,-1):
#     for s in range(0,num-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(0,num-i):
#         print(" ",end=" ")
#     for j in range(0,2*i+1):
#         print("*",end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num,0,-1):
#     for s in range(num-i):
#         print(" ",end=" ")
#     for j in range(0,2*i-1):
#         print("*",end=" ")
#     print()

# num=int(input("Enter a Number:"))
# for i in range(num):
#     print(" "*(num-i)+"* "*i)
# for i in range(num,0,-1):
#     print(" "*(num-i)+"* "*i)

# num=int(input("Enter a Number:"))
# for i in range(num+1):
#     for s in range(0,num-i):
#         print(" ",end=" ")
#     for j in range(0,2*i+1):
#         print("*",end=" ")
#     print()
# for i in range(num,0,-1):
#     for s in range(num-i+1):
#         print(" ",end=" ")
#     for j in range(0,2*i-1):
#         print("*",end=" ")
#     print()

for i in range(9):
    for j in range(13):
        if i==2 or i==6 or i+j==6 or j-i==6 or i-j==2 or i+j==14:
            print("*",end="")
        else:
            print(" ",end="")
    print()