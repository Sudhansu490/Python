# Wap to enter the mark of a student in 6 subjects then calculate the total mark, avg mark and grade.
#       avg>=90       -------> O Grade
# avg>=80 and avg<=89 -------> E Grade
# avg>=70 and avg<=79 -------> A Grade
# avg>=60 and avg<=69 -------> B Grade
# avg>=50 and avg<=59 -------> C Grade
# avg>=40 and avg<=49 -------> D Grade
# otherwise fail - Better Luck Next Time

phy=int(input('Enter phy mark :'))
chem=int(input('Enter chem mark :'))
mth=int(input('Enter mth mark :'))
eng=int(input('Enter eng mark :'))
IT=int(input('Enter IT mark :'))
hin=int(input('Enter hin mark :'))

totalmark=phy+chem+mth+eng+IT+hin
avgmark=totalmark/6

print('---------------------------')
print('Total mark is :',totalmark)
print('Average mark is :',avgmark)

if avgmark>=90:
    print('O Grade')
elif avgmark>=80 and avgmark<=89:
    print('E Grade')
elif avgmark>=70 and avgmark<=79:
    print('A Grade')
elif avgmark>=60 and avgmark<=69:
    print('B Grade')
elif avgmark>=50 and avgmark<=59:
    print('C Grade')
elif avgmark>=40 and avgmark<=49:
    print('D Grade')
else:
    print('fail - Better Luck Next Time')