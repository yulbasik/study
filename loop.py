smallest = None
largest = None
total = 0
while True:
    inpt = str(raw_input('Enter your number:'))
    if inpt == 'done':
        print 'Done!'
        break
    else:
        try:
            n = float(inpt[1:])
            total += n
            if n > largest or largest is None:
                largest = n
            if n < smallest or smallest is None:
                smallest = n
        except:
            print 'Wrong data, enter a number:'
print 'In total:', total,
print 'Max:', largest, 'Min:', smallest




