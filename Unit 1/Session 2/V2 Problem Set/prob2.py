#Problem 2: Average Score
'''Write a function average() that takes in a list of 
integers scores as a parameter and returns the average score.

def average(scores):
    pass
Example Usage:

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)
Example Output: 86.4'''

def average(scores):
    all=0
    for num in scores:
        all +=num
    
    return all/len(scores)

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)