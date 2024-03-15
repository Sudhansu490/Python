# Ex=1 
# a=100
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# assert a==100  # if the condition is true then execute remaining codes otherwise raise an exception & stop the flow of execution.
# print(7)
# print(8)
# print(9)
# print(10)

# Ex=2(It does show any description about the error)
# a=100
# print(1)
# print(2)
# print(3)
# a=23
# print(4)
# print(5)
# print(6)
# assert a==100  # AssertionError
# print(7)
# print(8)
# print(9)
# print(10)

# Ex=3(if we want to show any description about the error then we have to write like this)
# a=100
# print(1)
# print(2)
# print(3)
# a=23
# print(4)
# print(5)
# print(6)
# assert a==100,'a is not 100 it modified'
# print(7)
# print(8)
# print(9)
# print(10)

# Ex=4
# l=['sudhansu','saina','priyanka','swastika','prangya','lipshika']
# assert input('Enter Your Name:') in l,'this name is not present'
# print('ramaining codes')

# Ex=5
# l=['sudhansu','saina','priyanka','swastika','prangya','lipshika']
# try:
#     assert input('Enter Your Name:') in l,'this name is not present'
# except Exception as e:
#     print(e)
# print('Remaining codes')

# Ex=6(If we don't write any description about the error then it shows a blank line)
# l=['sudhansu','saina','priyanka','swastika','prangya','lipshika']
# try:
#     assert input('Enter Your Name:') in l
# except Exception as e:
#     print(e)
# print('Remaining codes')