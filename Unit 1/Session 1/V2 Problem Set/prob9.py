#Problem 9: Countdown
'''Write a function countdown() that takes in two positive 
integers m and n as parameters and prints numbers from m down
 to n.

def countdown(m,n):
    pass
Example Usage: countdown(5,1)

Example Output:

5
4
3
2
1'''

def countdown(m,n):

    for num in range(m,n-1,-1):
        print(num)
    # while m>=n:
    #     print(m)
    #     m -=1
        
countdown(5,1)
