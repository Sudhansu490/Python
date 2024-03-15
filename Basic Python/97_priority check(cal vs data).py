import cal
import data
print(cal.a)
print(data.a)

from cal import *
from data import *
print(a)  # last one have more priority

print(add(10,20))
print(sub(b,a))  # last one have more priority