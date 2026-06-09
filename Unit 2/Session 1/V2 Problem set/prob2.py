#Problem 2: Student Directory
'''Write a function student_directory() that takes a 
list of student_names as a parameter and returns a 
dictionary of students, 
where each student in student_names is a key mapped to a 
unique numerical 
;' ID.

def student_directory(student_names):
    pass
Example Input: student_names = ["Ada Lovelace", "Tu Youyou", 
"Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
Example Output: {"Ada Lovelace": 1, "Tu Youyou": 2, 
"Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}
'''

def student_directory(student_names):
    dictt={}
    for i in range (len(student_names)):
        dictt[student_names[i]] = i+1
    return dictt

# def student_directory(student_names):
#     student_dict = {}
#     student_id = 1  # Start student IDs at 1
#     for name in student_names:
#         student_dict[name] = student_id
#         student_id += 1
#     return student_dict

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))