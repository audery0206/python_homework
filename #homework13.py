#homework13
'''Write a function count_vowels(s) that counts the number of vowels (i.e., a, e, i, o, u) in a given string s. Ignore case sensitivity.
:
Input: s = "Hello World"
Output: 3
Explanation: The string s contains the vowels e, o, and o.
:
You can use a for loop and the in operator to iterate through each character in the string.
Convert the string to lowercase using s.lower() for easier comparison.
Use a variable to accumulate the count of vowels and return it at the end.
'''
string = str(input('please enter a string:'))
x=0
print(string.lower())
y=string.lower()
for letter in string.lower():
#    print(letter)
    if 'a' in letter:
        x=x+1
#        print(x)
    elif 'e' in letter:
        x=x+1
#        print(x)
    elif 'i' in letter:
        x=x+1
#        print(x)
    elif 'o' in letter:
        x=x+1
#        print(x)
    elif 'u' in letter:
        x=x+1
#        print(x)
    else :
        x=x
#        print(x)
print(x)