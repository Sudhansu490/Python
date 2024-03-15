# Also called Inner Dictionary.

# d={1:{'name':'sudhansu'},2:{'name':'lipshika'},3:{'name':'ananya'},4:{'name':'prangya'}}
# print(d)
# for i in d:
#     print(i)
# for i in d.values():
#     print(i)
# for i,j in d.items():
#     print(i,j)

# d={1:{'name':'sudhansu'},2:{'name':'lipshika'},3:{4:{5:{6:7}}}}
# print(d)
# d[3][4][5][6]=5000
# print(d[3][4][5][6])
# print(d)

# -----------------------------------------------------------------

# How to iterate a Nested Dictionary

studesnts={
    101:{'Name':'Sumit','Email':'sumit@gmail.com','Address':'Unit-6'},
    102:{'Name':'Puja','Email':'puja@gmail.com','Address':'Unit-8'},
    103:{'Name':'Lipshika','Email':'lipshika@gmail.com','Address':'Unit-1'},
    104:{'Name':'Ananya','Email':'ananya@gmail.com','Address':'Unit-9'}
}
for k,v in studesnts.items():
    print('Student ID is',k)
    for i in v:
        print(f'{i} is : {v[i]}')
    print('-'*25)