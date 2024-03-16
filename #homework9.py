#homework9
'''
Given a positive integer n, print numbers from 1 to n. However, for multiples of 3, print “Fizz” instead of the number, 
and for multiples of 5, print “Buzz”. 
For numbers that are multiples of both 3 and 5, print “FizzBuzz”. 

Sample when n = 15, 
output：
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''
x=1
n=15
while x <= n:
    #print(x)
    if (x%3 == 0 and x%5 == 0):
        print ('FizzBuzz')
    elif(x%3==0):
        print('Fizz')
    elif(x%5==0):
        print('Buzz')
    else:
        print(x)
    x=x+1


