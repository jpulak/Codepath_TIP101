#Problem 2: Fibonacci Cases
'''Given the base case and recursive case, write a function fibonacci() that returns the nth number in the fibonacci sequence. The Fibonacci sequence is a mathematical sequence of numbers where each number is the sum of the two preceding numbers.

Base Cases: Because Fibonacci numbers are defined by adding the two previous numbers in the sequence, the first two Fibonacci numbers are pre-defined. By definition, the 0th Fibonacci number is 0, and the 1st Fibonacci number is 1.

Recursive Case: The nth Fibonacci number is the n-1th Fibonacci number + the n-2th Fibonacci number.
d
def fibonacci(n):1
	pass
Example Usaage:

# Example Input: 6dd
Example Output:s

# Expected Output: 8d
# Explanation: The 6th Fibonacci number is 8. The 5th Fibonacci number is 5 and the 4th Fibonacci
# number is 3. 5 + 3 = 8.
'''

def fibonacci(n):
	if n ==0:
		return 0
	elif n ==1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)