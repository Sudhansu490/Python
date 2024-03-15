# for else


# for loop executed fully without having break

# for i in range(5):
#     print(i)
# else:
#     print('I am else block')

# if break executed inside for loop then our else block won't be executed.

for i in range(10):
    if i==5:
        break
    print(i)
else:
    print('I am else block')