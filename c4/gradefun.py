def get_grade(marks):
    grade = 'x'
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
    return grade


marks = input('Enter marks: ')
grade = get_grade(marks)

print 'Your grade: ' + grade
