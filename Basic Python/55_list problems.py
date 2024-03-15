# Q.1 wap to search a value from a list then display its index
# if the value is present multiple times then print its indices and
# also count the number of times that value is repeated in the list.

# l=[10,20,30,10,40,20,60,50,70,30,80,10,90]
# i=0
# count=0
# key=int(input("Enter a key:"))
# while i < len(l):
#     if key == l[i]:
#         print(f'{key} is present at {i} index')
#         count=count+1
#     i=i+1
# print(f'{key} is present {count} times.')



# Q.2 INPUT:
# l=['Hi','Hello']
# s=['Sonu','Ananya','Lipshika','Swastika']
# Excepted OUTPUT:
# ['Hi Sonu', 'Hi Ananya', 'Hi Lipshika', 'Hi Swastika', 'Hello Sonu', 'Hello Ananya', 'Hello Lipshika', 'Hello Swastika']

# l=['Hi','Hello']
# s=['Sonu','Ananya','Lipshika','Swastika']
# new_list=[]
# for i in l:
#     for j in s:
#         new_list.append(i+' '+j)
# print(new_list)



# Q.3 INPUT:
# l=['Pooja','Payal','Aditi','Stiti']
# Excepted OUTPUT:
# ['Pa','Pl','Ai','Si']

l=['Pooja','Payal','Aditi','Stiti']
new_list=[]
for i in l:
    new_list.append(i[0]+i[-1])
    # n=len(i)
    # new_list.append(i[0]+i[n-1])
print(new_list)