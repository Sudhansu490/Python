# 1.WAP to find out the number of occurrences of a character present in a string. 

# s='ananya'
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
# print(d)
# for i,j in d.items():
#     print(f'{i} is present {j} times.')

# s='aa bb cc dd' 
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
# print(d)

# --------------------------------------------------------------------------

# 2.WAP take BF and GF name as an input from the user.Store them in a dictionary then enter BF name to know GF name.

d={}
while True:
    bf=input('Enter BF Name: ')
    gf=input('Enter GF Name: ')
    d[bf]=gf
    choice=input('Do you want to add more item[Y/N]:').upper()
    if choice=='N':
        break
while True:
    bf=input('Enter BF Name to get GF Name:')
    gf=d.get(bf,0)
    if gf==0:
        print('Sry GF Name is not available.')
    else:
        print(f'Hi {bf} your GF Name is {gf}')
    choice=input('Do you want to search more item[Y/N]:').upper()
    if choice=='N':
        break