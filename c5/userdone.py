x = ''
while x != 'done':
    try:
        x = raw_input('Data: ')
    except Exception, e:
        print e
