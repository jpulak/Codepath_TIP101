#Problem 4: Keys Versus Values
'''Write a function keys_v_values() that takes in a 
dictionary dictionary whose keys and values are both 
integers. Using at least one loop, the function should find
 the sum of all keys in the dictionary and the sum of all 
 values.
If the sum of all keys is greater than the sum of all 
values, the function should return the string "keys".
If the sum of all values is greater than the sum of all 
keys, the function should return the string "values".
If keys and values have equal sums, the function should return 
the string "balanced".

def keys_v_values(dictionary):
    pass
Example Usage:

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
Example Output:

values
keys'''

def keys_v_values(dictionary):
    keys =0
    vals =0
    #sum of all keys through .keys()
    for i in dictionary.keys():
        keys += i
    #sum of all vals through.values()
    for i in dictionary.values():
        vals += i
    
    if keys>vals:
        return "Keys"
    elif vals>keys:
        return "Values"
    else:
        return "balanced"
# def keys_v_values(dictionary):
#     keys=0
#     vals=0
#     for i in dictionary:
#         keys +=i
#     values = dictionary.values()
#     vals = sum(values)
#     if keys > vals:
#         return "Keys"
#     else:
#         return "Values"
    
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
