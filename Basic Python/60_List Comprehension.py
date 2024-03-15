# l=[i for i in range(6)]
# print(l)

# l=[i*i for i in range(6)]
# print(l)

# l=[i**i for i in range(6)]
# print(l)

# l=[i+10 for i in range(6)]
# print(l)

# with using List Comprehension
# l=[i for i in range(21) if i%2==0]
# print(l)

# without using List Comprehension
# l=[]
# for i in range(0,21):
#     if i%2==0:
#         l.append(i)
# print(l)


# names=['sonu','titu','anu','swty']
# Excepted Output=['s','t','a','s']
# names=['sonu','titu','anu','swty']
# l=[i[0] for i in names]
# print(l)
# l=[i[0:3] for i in names]
# print(l)

# create a new list by adding the element which is containing letter 't'
# names=['sonu','titu','anu','swty']
# l=[i for i in names if 't' in i]
# print(l)

# create a new list by adding the element but if the element is 'anu' then print 'hello'
# names=['sonu','titu','anu','swty']
# l=[i if i!='anu' else 'hello' for i in names]
# print(l)


# create a list from tuple
# t=(10,20,30,40,50)
# l=[i for i in t]
# print(l)

# t=(10,20,30,40,50)
# l=[i for i in t if i%4==0]
# print(l)

# create a list from string
# name='sonu'
# l=[i for i in name]
# print(l)

# creation of matrix using list comprehension concept
# m=[[j for j in range(3)] for i in range(3)]
# print(m)
# m=[[i for j in range(3)] for i in range(3)]
# print(m)
# m=[[i*j for j in range(3)] for i in range(3)]
# print(m)