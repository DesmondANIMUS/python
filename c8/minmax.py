num = []
while True:
    x = raw_input('Data: ')
    if x == 'done':
        break
    num.append(x)

if len(num) > 0:
    print 'Max number: ' + str(max(num))
    print 'Min number: ' + str(min(num))
else:
    print 'Empty sequence'
