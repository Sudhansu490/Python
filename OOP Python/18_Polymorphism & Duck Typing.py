# Polymorphism- If one thing existed in a different form then it is called Polymorphism.
# print(10+20)  # Addition
# print('10'+'20')  # Concatenation

# --------------------------------------------------------------------------------------

# Duck Typing

# a=23
# print(type(a))
# a=23.45
# print(type(a))
# a='surendra'
# print(type(a))

# object(methods is important)
# class A:
#     def mt1(self):
#         print('A-mt1')
# class B:
#     def mt1(self):
#         print('B-mt1')
# class C:
#     def mt1(self):
#         print('C-mt1')
# def display(X):
#     X.mt1()
# a=A()
# display(a)
# b=B()
# display(b)

# class A:
#     def mt1(self):
#         print('A-mt1')
# class B:
#     def mt1(self):
#         print('B-mt1')
# class C:
#     pass
# def display(X):
#     X.mt1()
# c=C()
# display(c)  # AttributeError: 'C' object has no attribute 'mt1'