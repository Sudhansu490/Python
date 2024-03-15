# Set methods(used for mathematical operations)

# 1.union() -> used to return all the elements present in both set.
# A={10,20,30,40,50}
# B={40,50,60,70}
# print(A.union(B))
# print(A | B)

# 2.intersection() -> used to return all the common elements present in both set.
# A={10,20,30,40,50}
# B={40,50,60,70}
# print(A.intersection(B))
# print(A & B)

# 3.difference() -> used to return either all the elements present in set A not in set B or all the elements present in set B not in set A.
# A={10,20,30,40,50}
# B={40,50,60,70}
# print(A.difference(B))
# print(A - B)
# print(B.difference(A))
# print(B - A)

# 4.symmetric_difference() -> used to return all the elements present in set A or B but not in both.
# A={10,20,30,40,50}
# B={40,50,60,70}
# print(A.symmetric_difference(B))
# print(A ^ B)

# 5.subset & superset
# A={1,2,3,4,5,6,7,8,9}
# B={3,4,5,6}
# print(B.issubset(A))
# print(A.issubset(B))
# print(B.issuperset(A))
# print(A.issuperset(B))

# 6.disjoint set
# A={1,2,7,8,9}
# B={3,4,5,6}
# print(B.isdisjoint(A))
# print(A.isdisjoint(B))