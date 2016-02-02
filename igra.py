s = raw_input()
ss = raw_input()
# h = s.find('h', 0)
# e = s.find('e', h)
# l = s.find('l', e)
# l_2 = s.find('l', l + 1)
# o = s.find('o', l_2)
# if h < e < l and l < l_2 < o:
#     print 'YES'
# else:
#     print 'NO'
# # print h, e , l, l_2, o

t = s[::-1]
if ss == t:
    print 'YES'
else:
    print 'NO'
