# Example 1
# class A:pass
# class B(A):pass
# class C(A):pass
# class D(B):pass
# class E(C):pass
# class F(D,E):pass
# print(A.__mro__)  # A-object
# print(B.__mro__)  # B-A-object
# print(C.__mro__)  # C-A-object
# print(D.__mro__)  # D-B-A-object
# print(E.__mro__)  # E-C-A-object
# print(F.__mro__)  # F-D-B-E-C-A-object

# Ex-1 with Method Implementation
# class A:
#     def m1(self):
#         print('A-M1')
# class B(A):
#     def m1(self):
#         print('B-M1')
# class C(A):
#     def m1(self):
#             print('C-M1')
# class D(B):
#     def m1(self):
#         print('D-M1')
# class E(C):
#     def m1(self):
#         print('E-M1')
# class F(D,E):pass
# f=F()
# f.m1()  # as class F has no print statement so it prints class D print statement

# Example 2
# class A:pass
# class B:pass
# class C(A):pass
# class D(A):pass
# class F(B):pass
# class G(B):pass
# class E(C,D,F):pass
# print(E.__mro__)  # E-C-D-A-F-B-object

# Example 3
# class C:pass
# class A:pass
# class B:pass
# class D:pass
# class E:pass
# class K1(C,A,B):pass
# class K3(A,D):pass
# class K2(B,D,E):pass
# class Z(K1,K3,K2):pass
# print(K1.__mro__)
# print(K3.__mro__)
# print(K2.__mro__)
# print(Z.__mro__)