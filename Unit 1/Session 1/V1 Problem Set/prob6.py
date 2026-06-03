#Problem 6: Classify Age
'''Write a function classify_age() that takes an integer age as a parameter and returns "child" if the age is less than 18, and returns "adult" otherwise.

Example Usage:

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
Output:

adult
child
adult'''

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)