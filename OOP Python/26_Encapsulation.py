# Encapsulation is a mechanism of wraping the data & methods into a single unit.
# It prevents Accidental Modification.
# The Attributes of a class will be hidden from other classes & It can be access only by using methods of their current class.

# Accidental Modification
# class College:
#     def __init__(self):
#         self.balance=5000000
# c=College()
# print(c.balance)
# c.balance=50
# print(c.balance)

# Prevent accidental modification
# class College:
#     def __init__(self):
#         self.__balance=5000000  # Data Hiding
# c=College()
# print(c.balance)  # AttributeError: 'College' object has no attribute 'balance'
# print(c.__balance)  # AttributeError: 'College' object has no attribute '__balance'

# class College:
#     def __init__(self):
#         self.__balance=5000000  # Private Attribute
#     def getBalance(self,password):
#         if password==2002 or password==2020:
#             return self.__balance
#         else:
#             return 'Invalid User'
# c=College()
# print(c.getBalance(2020))  
# print(c.getBalance(2023))  # Invalid User