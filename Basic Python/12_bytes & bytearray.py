# 1.bytes datatype
a=[10,20,30]   # list
b=bytes(a)   # list to bytes
# print(b[0])
# print(b[4])
# print(b[-2])

# for i in b:
#     print(i)


# 2.bytearray datatype
a=[10,20,30,40,50]
b=bytearray(a)   # convert list to bytearray
# print(b[1])
# print(b[-1])

# for i in b:
#     print(i)

# Modification of index value
b[1]=99
b[2]=7
for i in b:
    print(i)