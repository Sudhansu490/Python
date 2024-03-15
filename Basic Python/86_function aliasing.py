# def calculations(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a%b)
# print('Before aliasing')
# calculations(10,2)
# cal=calculations
# print('After aliasing')
# cal(10,2)

# if we delete original function name(i.e calculations), then still we can call the function by using alias name(i.e cal).
# def calculations(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a%b)
# print('Before aliasing')
# calculations(10,2)
# cal=calculations
# del calculations
# print('After aliasing')
# cal(10,2)
# calculations(50,5)  # NameError

# All the alias names are points to same memory location. We can call the function by using any alias name.
def calculations(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
cal=calculations
cl=cal
c=cl
print(id(calculations))
print(id(cal))
print(id(cl))
print(id(c))
c(50,5)