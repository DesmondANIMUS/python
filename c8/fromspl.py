count = 0
for line in open('./data.txt'):
    if line.startswith('From'):
        print line.split(' ')[1]
        count += 1
print '\nThere were ' + str(count) + ' lines in file starting with From'
