#homework16
'''Question 1: 
: Given a list of integers, use the filter function to create an iterator that only includes the even numbers in the list.
Input: [3, 1, 2, 4, 5]
Output: [2, 4]'''
#--------------------------
numbers = [3,1,2,4,5]
even_number = [
    number
    for number in numbers
    if number%2==0
]
print(even_number)