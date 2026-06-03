#Problem 11: Counter
'''Write a function counter() that uses the range 
function to print numbers between 1 and a given stop value
 (inclusive).

def counter(stop):
    pass
Example Usage: counter(7). Example Output:

1
2
3
4
5
6
7'''

def counter(stop):
    for i in range (1,stop+1):
        print(i)

n= int(input('provide number: '))

counter(n)

print(counter(7))
