# class Outer:
#     def __init__(self):
#         print('Outer Class Constructor')
#     class Inner:
#         def __init__(self):
#             print('Inner Class Constructor')
# o=Outer()  # Outer class object creation
# # i=Inner()  # NameError: name 'Inner' is not defined
# i=o.Inner()  # Inner class object creation using Reference variable
# i1=Outer.Inner()  # Inner class object creation using class name
# i2=Outer().Inner()  # first it create Outer class object then create Inner class object

# Inner class object creation inside Outer class
# class Outer:
#     def __init__(self):
#         print('Outer Class Constructor')
#     class Inner:
#         def __init__(self):
#             print('Inner Class Constructor')
#     i=Inner()
# o=Outer()  

# One Outer class can contain multiple Inner class.
# class Outer:
#     def __init__(self):
#         print('Outer Class Constructor')
#     class Inner1:
#         def __init__(self):
#             print('Inner1 Class Constructor')
#     class Inner2:
#         def __init__(self):
#             print('Inner2 Class Constructor')
# o=Outer()
# i1=o.Inner1()
# i2=o.Inner2()

# Inner Inner class
class Outer:
    def __init__(self):
        print('Outer Class Constructor')
    class Inner:
        def __init__(self):
            print('Inner Class Constructor')
        class InnerInner:
            def __init__(self):
                print('InnerInner Class Constructor')
o=Outer()
i=o.Inner()
ii=i.InnerInner()