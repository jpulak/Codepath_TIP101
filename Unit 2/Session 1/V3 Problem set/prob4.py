#Problem 4: Check for Number
'''Write a function attendance_rate() that takes 
in a dictionary attendance_list as a parameter.
 The function maps student names to their attendance status 
 ("Present" or "Absent"), and returns the percentage of 
 students who are present.

def attendance_rate(attendance_list):
	pass
Example Usage:

attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))
Example Output: 50.0 '''

def attendance_rate(attendance_list):
	pres =0
	abss =0
	for stuff,val in attendance_list.items():
		if val == "Present":
			pres += 1
		else:
			abss +=1
	return 100* (pres/(pres + abss))

attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))