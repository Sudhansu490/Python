num=int(input("Enter a Number:"))
prime=True

for i in range(2,num):
    if(num%i==0):
        prime=False
        break

if prime:
    print("The given Number is Prime.")
else:
    print("The given Number is not Prime")