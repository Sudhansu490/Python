# work with multiple class

# class Student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
#     def printDetails(self):
#         print('***STUDENT INFORMATION***')
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Roll No is {self.roll}')
#         print('-'*25)
# class Faculty:
#     def __init__(self,name,age,fid):
#         self.name=name
#         self.age=age
#         self.fid=fid
#     def printDetails(self):
#         print('***FACULTY INFORMATION***')
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Faculty ID is {self.fid}')
#         print('-'*25)
# s1=Student('Mohit',21,2001297198)
# s1.printDetails()
# f1=Faculty('Surendra',27,2024)
# f1.printDetails()
# s2=Student('Sujit',20,2001297200)
# f1.printDetails()

# -------------------------------------

# work with multiple objects

class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
names=['sonu','rahul','puja','stiti','monali','anita','soma','kirti']
age=[25,20,24,23,21,22,27,29]
roll=[1024,2024,3024,4024,5024,6024,7024,8024]
obj_list=[]
for i in range(len(names)):
    s=Student(names[i],age[i],roll[i])
    obj_list.append(s)
for i in range(len(names)):
    print(obj_list[i].name)
    print(obj_list[i].age)
    print(obj_list[i].roll)
    print('-'*15)