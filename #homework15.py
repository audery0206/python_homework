#homework15
'''Question 2: Dynamic Programming Calculation of Fibonacci Sequence
Difficulty: Medium
Description: Same as the previous question, we are dealing with the Fibonacci sequence. 
This time, please calculate the nth term of the Fibonacci sequence using dynamic programming and optimize the space complexity to O(1).
Example:
Input: n = 20
Output: 6765'''
#費氏數列 using iterative(dynamic program)用記憶體換時間
n=int(input("enter a number for verify Fibonacci sequence:"))
f={
    1:1,
    2:1,
}
for i in range(3, n+1):
    f[i]=f[i-1]+f[i-2]
#print(f.value(n))
#print(f"The Fibonacci value of {n} is: {f[n]}") -> 為何大掛號會印出來？
print(f[n])