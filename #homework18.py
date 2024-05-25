#homework18
'''Question 3: 
Given a dictionary that includes values for height and weight (in centimeters and kilograms), 
use a dictionary comprehension to convert the unit of height to meters and create a new dictionary.
Input: {"height": 175, "weight": 75}
Output: {'height': 1.75, 'weight': 75}'''
#---------------------------
input = {
    'height' : 175,
    'weight' : 75,
}
output ={
    key: (
        float(value/100)
        if key == 'height'
        else value
    )
    for key, value in input.items()
        
}
print(output)