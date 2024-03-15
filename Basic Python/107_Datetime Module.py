import datetime as dt

# working with Date
# d=dt.date(2023,5,19)
# print(d)
# print(d.year)
# print(d.month)
# print(d.day)

# working with Time
# t=dt.time(10,33,16,695286)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# working with both Date & Time
# DT=dt.datetime(2023,5,19,10,33,16,695286)
# print(DT)

# How to know current Date & Time
# current_DT=dt.datetime.now()
# print(current_DT)

# wap to wish the user based on the data
# 4-11 => Good Morning
# 11-17 => Good Afternoon
# 17-21 => Good Evening
# 21-4 => Good Night
# current_DT=dt.datetime.now()
# hr=current_DT.hour  # it will collect hour
# if hr>=4 and hr<11:
#     print('Hi...Good Morning')
# elif hr>=11 and hr<17:
#     print('Hey...Good Afternoon')
# elif hr>=17 and hr<21:
#     print('Hello...Good Evening')
# else:
#     print('Bye...Good Night')

# Customization on Date & Time
# current_DT=dt.datetime.now()
# print(current_DT.strftime('%a'))
# print(current_DT.strftime('%A'))
# print(current_DT.strftime('%W'))
# print(current_DT.strftime('%w'))
# print(current_DT.strftime('%m'))