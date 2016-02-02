inp = raw_input()
ones = str('1' * 7)
zer = str('0' * 7)
if ones in inp:
    print 'YES'
elif zer in inp:
    print 'YES'
else:
    print 'NO'
