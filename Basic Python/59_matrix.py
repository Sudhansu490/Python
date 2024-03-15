# Nested List as matrix

l= [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

# print in row wise
# for i in l:
#     print(i)

# print the matrix without comma & square bracket
for i in l:
    for j in i:
        print(j,end=' ')
    print()