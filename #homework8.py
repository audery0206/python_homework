#homework8
'''
You are given several lines of input, each containing a command followed by its arguments. 
The commands and arguments are separated by spaces. 
Implement a Python program to parse the input and execute the commands accordingly.

input() - Takes user input as a string.
input() should return 'hi i am good'.
name = input( - Takes user input as a string and assigns it to the variable name.
name = input( should prompt "Please enter your name" and if the user inputs "kk", name should be assigned the value "kk".
age = int(input( - Takes user input as an integer and assigns it to the variable age.
age = int(input( should prompt "Please enter your age" and if the user inputs "25", age should be assigned the integer value 25.
student_id = input( - Takes user input as a string and assigns it to the variable student_id.
student_id = input( should prompt "Please enter your student ID" and if the user inputs "b0123456789", student_id should be assigned the value "b0123456789".
def execute_commands(inputs: List[str]) -> None:
pass

A list of strings where each string represents a command and its arguments.
Print formatted with the variables name, student_id, and age.
'''
name = input('please enter your name :')
age = int(input('please enter your age:'))
student_id = input ('please enter your student ID :')
print('name:',name)
print('age :',age)
print('student_ID :', student_id)
