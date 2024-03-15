# Nested Function(Inner Function)

# def outer_fun():
#     print('I am inside outer_fun().')
#     def inner_fun():
#         print('I am inside inner_fun().')
#     inner_fun()
# outer_fun()

# It is not possible to call Inner Function outside of Outer function.We can call it only inside the Outer Function.
def outer_fun():
    print('I am inside outer_fun().')
    def inner_fun():
        print('I am inside inner_fun().')
    inner_fun()
outer_fun()
# inner_fun()  # NameError