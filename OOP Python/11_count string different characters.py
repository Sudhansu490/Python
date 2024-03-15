# count the number of uppercase,lowercase,vowels,digits,space and special symbols from a given string.

class String:
    def __init__(self):
        self.msg=input('Enter Any String:')
        self.uppercase=0
        self.lowercase=0
        self.vowels=0
        self.digits=0
        self.space=0
        self.specialsymbols=0
    
    def count_uppercase(self):
        for i in self.msg:
            if i.isupper():
                self.uppercase=self.uppercase+1
    def count_lowercase(self):
        for i in self.msg:
            if i.islower():
                self.lowercase=self.lowercase+1
    def count_vowels(self):
        for i in self.msg:
            if i in ('a','e','i','o','u','A','E','I','O','U'):
                self.vowels=self.vowels+1
    def count_digits(self):
        for i in self.msg:
            if i.isdigit():
                self.digits=self.digits+1
    def count_space(self):
        for i in self.msg:
            if i.isspace():
                self.space=self.space+1
    def count_specialsymbols(self):
        for i in self.msg:
            if i.isalpha():
                pass
            elif i.isdigit():
                pass
            elif i.isspace():
                pass
            else:
                self.specialsymbols=self.specialsymbols+1

    def call_all(self):
        self.count_uppercase()
        self.count_lowercase()
        self.count_vowels()
        self.count_digits() 
        self.count_space()
        self.count_specialsymbols()

    def printDetails(self):
        print('-'*35) 
        print(f'UpperCase = {self.uppercase}') 
        print(f'LowerCase = {self.lowercase}')       
        print(f'Vowels = {self.vowels}')       
        print(f'Digits = {self.digits}')    
        print(f'Space = {self.space}')    
        print(f'Special Symbols = {self.specialsymbols}') 

s=String() 
s.call_all()
s.printDetails()            