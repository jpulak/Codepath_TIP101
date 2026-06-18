#Problem 5: String Compression
'''Write a function that takes in a string my_str as a 
parameter and performs basic string compression using counts
 of repeated characters.

For example, the string "aabcccccaaa" would become "a2b1c5a3". 
If the compressed string does not become smaller than the 
original string, return the original string. Assume the string 
 has alphabetic characters.

def compress_string(my_str):
    pass
Example Usage:

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)
Example Output:

a5b2c3d1
abcde 
# did not convert my_str2 because `a1b1c1d1e1` is double the 
# length

'''
