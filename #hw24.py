#hw24
'''
Question 3:  Handling Index Out of Range
Description:  
# Given a function that takes a list and an index, 
and tries to return the element at that index. 
If the index is out of range, 
catch the error and return "Index out of range".

Program：
def get_list_element(lst, index): 
  # Write your code here
pass

Example:
print(get_list_element([1, 2, 3], 5)) 
# Should return "Index out of range"
'''
#LUT, index error.
user_list=input('enter a list(space-separated values):')
index=int(input('which index do you want to choose:'))
def get_list_element(user_list, index): 
    try:
        list_items = user_list.split(' ')
        return list_items[index]
    except IndexError:
        return 'Index out of range'

result = get_list_element(user_list, index)
print('number=', result)