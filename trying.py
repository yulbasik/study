word = 'From stephen.marquard@ uct.ac.za Sat Jan 5 09:14:16 2008'
pos = word.find('@') + 1
pos_2 = word.find(' ', pos+1)
replace = word.replace('r', 'Hello', 2)
print word[pos:pos_2]
print replace