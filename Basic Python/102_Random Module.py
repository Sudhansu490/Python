import random as r
# print(dir(r))
# help(r)

# randint() => It will generate a random int number between two specific number.
# val=r.randint(1,10)  # both 1 & 10 are included
# print(val)

# random() => It will generate a random float value between 0 to 1
# val=r.random()
# print(val)
# help(r.random)

# randrange() => exactly same as randint() but here stop value is not include
# val=r.randrange(1,10)  # here 10 is not include
# print(val)

# shuffle()
# l=[10,20,30,40,50]
# r.shuffle(l)
# print(l)
# help(r.shuffle)

# uniform() => It will generate a float value in a given range.
# val=r.uniform(10,20)
# print(val)
# help(r.uniform)

# sample() => It will generate samples from given data. 
# g=['ananya','lipshika','saina','prangya','swastika','pujitaa','swagatika']
# gf=r.sample(g,3)
# print(gf)
# data=r.sample(range(1000),5)
# print(data)

# choice()
# l1=[1,2,3,4,5,6]
# val=r.choice(l1)
# print(val)
# l2=r.choice(range(10000))
# print(l2)
# help(r.choice)