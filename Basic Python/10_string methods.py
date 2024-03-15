# 1.casechecking starting & ending of string(startswith(),endswith())
# msg='welcome to python programming language'
# print(msg.startswith('welcome'))
# print(msg.startswith('Welcome'))  # False,as case sensitive
# print(msg.endswith('language'))
# print(msg.endswith('abcd'))

# 2.checking what type of char is present on the given string(isalnum(),isalpha(),isdigit(),islower(),isupper(),istitle(),isspace() etc.)
# s='123python'
# print(s.isalnum())
# s='123python'
# print(s.isalpha())
# s='123'
# print(s.isdigit())
# s='123python'
# print(s.islower())
# s='PYTHON'
# print(s.isupper())
# s='Python Language'
# print(s.istitle())  # if first letter of each word is capital then its True.
# s="  "
# print(s.isspace())

# 3.change case(upper(),lower(),swapcase(),title(),capitalize() etc.)
# s='Python programming language'
# print(s.upper())
# print(s.lower())
# print(s.swapcase())  # lower cases becomes upper case & vice versa.
# print(s.title())  # converts the 1st char of each word to uppercase & other chars to lowercase.
# print(s.capitalize())  # coverts the 1st char of the sentence to uppercase & other chars to lowercase.

# 4.find out the length & count its occurence(len(),count())
# s='Python Programming Language'
# print(len(s))
# print(s.count('a'))
# print(s.count('a',17))

# 5.Replacement of string(replace())
# s='Python is a bad language'
# print(s.replace('bad','good'))

# 6.splitting of string(split())
# s='Surendra Kumar Panda'
# print(s.split())
# print(s.split('a'))
# dob='25-11-2002'
# print(dob.split('-'))
# print(dob.split('*'))  # as * is not present then it returns the original string.

# 7.joining the string(join())
# l=['sonu','ananya','lina']
# s1=''.join(l)
# print(s1)
# s2=' '.join(l)
# print(s2)

# 8.remove space from the string(strip(),lstrip(),rstrip() etc.)
# s='   sudhansu    '
# print(len(s))
# print(len(s.strip()))
# print(len(s.lstrip()))
# print(len(s.rstrip()))

# 9.fill character(ljust(),rjust(),center(),zfill() etc.)
# s='sudhansu'
# print(s.ljust(20,'*'))
# print(s.rjust(20,'-'))
# print(s.center(20,'*'))
# print(s.center(21,'*'))
# print(s.zfill(20))
# print(s.zfill(5))

# 10.other methods(isidentifier(),sorted(),min(),max(),enumerate() etc.)
# s1='sudhansu'
# print(s1.isidentifier())
# s2='123sonu'  # identifier name should not started with digits.
# print(s2.isidentifier())  # False
# s='sudhansu'
# print(sorted(s))
# print(sorted(s,reverse=True))
# s='sudhansu'
# print(min(s))
# print(max(s))
# s='sonu'
# for i in enumerate(s):
#     print(i)
# for i,j in enumerate(s):
#     print(i,j)