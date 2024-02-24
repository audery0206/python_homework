#homework5
#1. Intersection of Two Sets Given two sets of integers, 
#write a function that returns the intersection of them as a new set. 
#Example: Input: set_1 = {1, 2, 3, 4}, set_2 = {2, 4, 6, 8} Output: {2, 4}
set_1 = {1,2,3,4}
set_2 = {2,4,6,8}
x=set_1.intersection(set_2)
print(x)
#2. Union of K Sets Given a list of k sets of integers, 
#write a function that returns the union of all the sets as a new set. 
#Example: Input: sets = [{1, 2, 3}, {2, 4, 6}, {3, 5, 7}] Output: {1, 2, 3, 4, 5, 6, 7}
set_5 = {1,2,3}
set_6 = {2,4,6}
set_7 = {3,5,7}
j = set_5.union(set_6)
k = set_7.union(j)
print(k)

#3. Symmetric Difference of Two Sets Given two sets of integers, write a function that returns the symmetric difference of them as a new set. 
#The symmetric difference of two sets is the set of elements that are in either of the two sets, but not in both. 
#Example: Input: set_1 = {1, 2, 3, 4}, set_2 = {2, 4, 6, 8} Output: {1, 3, 6, 8}
set_3 = {1,2,3,4}
set_4 = {2,4,6,8}
y=set_3.difference(set_4)
z=set_4.difference(set_3)
#print(y)
#print(z)
h=y.union(z)
print(h)