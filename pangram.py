numb = int(raw_input())
inp = raw_input()
word = inp.lower()
# alp = 'abcdefghijklmnopqrstuvwxyz'
# count = 0
# for letter in alp:
#     hm = word.count(letter, 0)
#     if hm > 0:
#         count += 1
# if count >= 26:
#     print 'YES'
# else:
#     print 'NO'

seen = set()
for letter in inp:
    seen.add(letter)
if len(seen) == 26:
    print 'YES'
else:
    print 'NO'
