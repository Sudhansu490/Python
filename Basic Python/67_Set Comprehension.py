# create a set from list using set comprehension
# l=[10,20,30,40,50]
# s={i for i in l}
# print(s)

# from range()
# s={i for i in range(11)}
# print(s)

# create a set by adding all the element from 20 to 40 which is divisible by 4
# s={i for i in range(20,41) if i%4 == 0}
# print(s)

# create a set from list called as names by adding the first char of each element
# names=['Sonu','Munu','Anu','Lipsa']
# s1={i for i in names}
# print(s1)
# s2={i[0] for i in names}  # first letter
# print(s2)
# s3={i[0].lower() for i in names}  # first letter in small 
# print(s3)

# create a set from list(names) by adding all the elements but if the element is 'Munu' then instead of 'Munu' add 'Puja'
# names=['Sonu','Munu','Anu','Lipsa']
# s={i if i!='Munu' else 'Puja' for i in names}
# print(s)