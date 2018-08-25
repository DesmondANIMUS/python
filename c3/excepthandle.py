try:
    hours = input('Hours: ')
    rate = input('Rate: ')

    if hours > 40:
        pay = hours * rate * 1.5
        print 'Pay: ' + str(pay)
    else:
        pay = hours * rate
        print 'Pay: ' + str(pay)

except Exception, e:
    print "Exception caught: " + str(e)
