def count_grade(hours, rate):
    return hours * rate


hours = input('Hours: ')
rate = input('Rate: ')

print 'Pay: ' + str(count_grade(hours, rate))
