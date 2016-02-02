# my_file = open('story.txt', 'w')
# begining = 'This is my first attemp to write some file through python. I am very exited. In general I am a very happy girl.\nThanks God!'
# my_file.write(begining)
# my_file.close()

file = raw_input('Enter the name of your text file:')
if file == 'na na boo boo':
    print 'NA NA BOO BOO to you, you have been punk.d'
else:
    try:
        count = 0
        total = 0.0
        fhand = open(file)
        for line in fhand:
            line = line.strip()
            if line.startswith('X-DSPAM-Confidence:'):
                count += 1
                pos_1 = line.find(':')
                fl = float(line[pos_1+1:])
                total += fl
        average = total / max(count, 1)
        print 'Average spam confidence: %s' % average
    except:
        print 'sorry, no such find is found'



