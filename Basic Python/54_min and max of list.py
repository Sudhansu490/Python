# find out min and max value from a list

l=[4,3,10,2,1,8]
min=l[0]
for i in l:
    if i<min:
        min=i
print('Minimum number is = ',min)


l=[4,3,10,2,1,8]
max=l[0]
for i in l:
    if i>max:
        max=i
print('Maximum number is = ',max)