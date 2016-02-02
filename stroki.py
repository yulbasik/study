inp = raw_input()
stroka = inp.lower().translate(None, 'aeiouy')
new = ''
for i in range(0, len(stroka)):
        letter = stroka[i]
        new += '.' + letter
print new


