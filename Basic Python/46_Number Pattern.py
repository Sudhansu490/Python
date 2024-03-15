# Type 1
# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(i+1):
#         print(num-i,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(i+1):
#         print(num-j,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(i,-1,-1):
#         print(num-j,end=" ")
#     print()

# -------------------------------------------

# Type 2
# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(num-i,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(num-j,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):
#         print(num-j,end=" ")
#     print()

# ----------------------------------------

# Type 3
# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(num-i):
#         print(j+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(num-i):
#         print(i+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(num-i):
#         print(i+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(num-i):
#         print(num-i,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(num-i):
#         print(num-j,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for j in range(num-i-1,-1,-1):
#         print(num-j,end=" ")
#     print()

# ------------------------------------------------

# Type 4
# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(num-i):
#         print(j+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(num-i-1,-1,-1):
#         print(j+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(num-i):
#         print(i+1,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(num-i):
#         print(num-i,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(num-i):
#         print(num-j,end=" ")
#     print()

# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(num-i-1,-1,-1):
#         print(num-j,end=" ")
#     print()

# ----------------------------------------------

# Type 5
# num=int(input("Enter the Number of rows:"))
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
# # remove the space of empty space'end'of the Type 2 then we get our Triangle pattern.

# reverse of Type 5
num=int(input("Enter the Number of rows:"))
for i in range(num-1,-1,-1):
    for s in range(num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
# remove the space of empty space 'end' of the Type 2 & change the range of i(num => num-1,-1,-1) then we can get our Triangle pattern.