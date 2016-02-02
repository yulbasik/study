# # ex. 9.2
# fname = raw_input('Enter file name: ')
# if len(fname) < 1: fname = 'mbox-short.txt'
# fhand = open(fname)
# lst = []
# dic = {}
# for line in fhand:
#     line = line.strip()
#     if line.startswith('From '):
#         l = line.split()
#         lst.append(l[2])
#         for x in lst:
#             dic[x] = dic.get(x, 0) +1
# print dic

#Ex. 9.3
fname = raw_input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
fhand = open(fname)
lst = []
dic = {}
for line in fhand:
    line = line.strip()
    if line.startswith('From '):
        l = line.split()
        lst.append(l[1])
for x in lst:
    dic[x] = dic.get(x, 0) +1
li = dic.values()
m = max(li)
for key in dic:
    if dic[key] == m:
        print key, m



# import string
#
# n = raw_input('Enter file name: ')
# if len(n) < 1:
#     n = "romeo.txt"
# fname = open(n)
# l = []
#
# for x in fname:
#     x = x.strip()
#     x = x.translate(None, string.punctuation)
#     x = x.lower()
#     part = x.split()
#     l.extend(part)
# end = dict((el, 0) for el in l)
# print l


# st = 'brontosaurus'
# d = dict()
# for c in st:
#     d[c] = d.get(c, 0) + 1
# print d







