grade = 'x'
marks = input('Enter marks: ')
if marks < 0.0 and marks > 1.0:
    print('Out of range')
else:
    if marks >= 0.9:
        grade = 'A'
    elif marks >= 0.8 and marks < 0.9:
        grade = 'B'
    elif marks >= 0.7 and marks < 0.8:
        grade = 'C'
    elif marks >= 0.6 and marks < 0.7:
        grade = 'D'
    else:
        grade = 'E'
print 'Your grade is: ' + grade
