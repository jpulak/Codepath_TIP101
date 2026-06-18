#Problem 4: Reverse Sentence
'''Write a function reverse_sentence() that takes in 
 string sentence as a parameter and returns the string
   with the sentence but with the order of the words
     reversed. The sentence will only contain alphabetic 
     characters and spaces to separate the words. If 
     there is only one word in the sentence, the function 
     returns the original string.

def reverse_sentence(sentence):
    pass
Example Input: sentence = "I solemnly swear I am up to no good"

Example Output: "good no to up am I swear solemnly I"

'''

def reverse_sentence(sentence):
    res=""
    new = sentence.split()

    #used no functions
    for word in new:
        res = word +" "+ res
    return res

    # return (" ".join(new[::-1]))

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))