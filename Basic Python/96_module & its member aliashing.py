# Giving another name to module is called module alishing.
# Module aliashing

# import calculation as cal
# print(cal.add(20,30))
# print(cal.pi)
# print(calculation.sub(20,10))  # NameError

# different ways of importing modules
# from calculation import add,sub
# print(add(5,7))
# print(sub(7,3))
# print(mul(5*2))  # NameError(bcoz we are not importing mul())

# from calculation import *
# print(add(5,7))
# print(sub(7,3))
# print(mul(5,2))
# print(div(10,2))

# --------------------------------------------------------------

# Module member aliashing

# from calculation import add as a,sub as s, pi as p
# print(a(20,25))
# print(s(25,10))
# print(p)
# print(pi)  # NameError