#homework14
'''Question 1: Recursive Calculation of Fibonacci Sequence
Difficulty: Easy
Description: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1. 
Given a positive integer n, please calculate the nth term of the Fibonacci sequence using recursion.
Example:
Input: n = 5
Output: 5'''

#費氏數列 using recursion,用時間換取空間（記憶體）
#x=0,1,1,2,3,5,8,13,21....
'''
n=input()
for i in range(3,n+1)
    i=0, f(0)=0
    i=1, f(1)=1
    f(i)=f(i-1)+f(i-2)
'''
x=int(input("enter a number for verify Fibonacci sequence:"))
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(x))
