#Problem 8: Multiples of Five
'''Write a function multiples_of_five() 
that prints out multiples of 5 between 1 and 100 (inclusive).

def multiples_of_five():
    pass
Example Output:

5
10
15
20
25
....
90
95
100
'''

def multiples_of_five():
    for i in range(5,101,5):
        print(i)

    # for num in range(5,101):
    #     if num%5 ==0:
    #         print(num)


print(multiples_of_five())