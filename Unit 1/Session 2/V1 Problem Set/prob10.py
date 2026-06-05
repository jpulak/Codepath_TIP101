#Problem 10: FizzBuzz
'''Write a function fizzbuzz() that takes in an integer n as 
a parameter and prints the numbers from 1 to n.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.

def fizzbuzz(n):
    pass
Example Usage: fizzbuzz(13)

Example Output:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13'''

def fizzbuzz(n):
    for i in range(1, n+1):
        if i%3 ==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
            continue
        elif i%5 ==0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(20)