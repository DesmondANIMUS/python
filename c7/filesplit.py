numbers = []
fname = raw_input('Enter file name: ')
for line in open(fname):
    if line.startswith('X-DSPAM-Confidence:'):
        numbers.append(float(line.split(':', 2)[1].strip()))
print 'Average spam confidence: ' + str(sum(numbers) / len(numbers))
