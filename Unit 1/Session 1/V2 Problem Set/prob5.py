#Problem 5: Calculate Tip
'''Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
If service_quality is "poor", the function should return 10% 
of the bill value.
If service_quality is "average", the function should return 15% 
of the bill value.
If service_quality is "excellent", the function should return 20%
 of the bill value.
If service_quality is any other value, the function should 
return None.

def calculate_tip(bill, service_quality):
    pass
Example Usage:

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
Example Output:

6.6795
4.453
8.906'''

def calculate_tip(bill, service_quality):
    if service_quality == 'poor':
        return bill*.10
    elif service_quality =='average':
        return bill*.15
    elif service_quality =='excellent':
        return bill*.2
    else:
        return None
        # pass

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)

print(calculate_tip(44.53, "meh"))