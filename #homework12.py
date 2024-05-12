#homework12
'''Write a function is_prime(n) that determines whether a positive integer n is a prime number.
If it is, return True; otherwise, return False.
:
Input: n = 17
Output: True
Explanation: 17 is only divisible by 1 and 17, so it is a prime number.
:
You can use a for loop and the range function to iterate through possible factors of n.
If n is divisible by any positive integer less than n, it is not a prime number.
You can use the modulo operator (n % x) to check if n is divisible by x. 
If the remainder is 0, it means n is divisible by x.
nested loop
'''
check=False
n=int(input('please enter a number:'))
#for x in range(1, n+1):
#print('n=',n)
for j in range(2, n):
#    print('j=', j)
    if n%j==0 :
        print(n,'is not a prime number')
        check=True 
        break
#    else : 
if check == False:
    print(n,'is a prime number')