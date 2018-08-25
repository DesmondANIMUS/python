hours = input('Hours: ')
rate = input('Rate: ')

if hours > 40:
    pay = hours * rate * 1.5
    print 'Pay: ' + pay
else:
    pay = hours * rate
    print 'Pay: ' + pay
