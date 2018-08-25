data = []
for line in open('./data.txt'):
    data.extend(line.split(' '))
print data
