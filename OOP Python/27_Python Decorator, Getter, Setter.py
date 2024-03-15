# Python Decorators
# A Decorator is a function that takes another function as an argument and returns a new function that modifies the behaviour of the original function.
# The new function is often reffered to as a 'Decorated' function.

# Ex=1(Type 1)
# def greet(fx):
#     def mfx():
#         print('Good Morning')
#     fx()
#     print('Thanks for using this function.')
#     return mfx
# @greet
# def hello():
#     print('Hello World')
# hello()

# Ex=1(Type 2)
# def greet(fx):
#     def mfx():
#         print('Good Morning')
#     fx()
#     print('Thanks for using this function.')
#     return mfx
# def hello():
#     print('Hello World')
# greet(hello)()

# Ex=2(Here the 'fx' function is the original function that we pass an argument to the 'greet' decorator.It's the function that we intend to modify with the decorator.In the case of 'hello()' function,'fx' refers to the 'hello()' & in the case of 'add(a,b)','fx' refers to the 'add(a,b)' function.)
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print('Good Morning')
#         fx(*args,**kwargs)
#         print('Thanks for using this function.')
#     return mfx
# @greet
# def hello():
#     print('Hello World')
# hello()
# def add(a,b):
#     print(a+b)
# greet(add)(1,2)

# ------------------------------------------------------------------

# Getters & Setters
# Getters in python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property & are typically defined using the @property decorator.
# Getters do not take any parameters & we can't set the value through Getter method. For that we need Setter method which can be added by decorating method with @property_name.setter.
# In conclusion, Getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden.This can be useful for encapsulation & data validation.
class myClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f'value is {self._value}')
    @property
    def ten_value(self):
        return 10*self._value
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
obj=myClass(10)
obj.show()
obj.ten_value=65  # update the ten_value from 100 to 65
print(obj.ten_value)
obj.show()