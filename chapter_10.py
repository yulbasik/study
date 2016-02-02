# prints the 10 most common words in a file
# import string
# fname = raw_input('enter file name: ')
# if len(fname) < 1:
#     fname = 'romeo.txt'
# fhand = open(fname)
# dic = {}
# for line in fhand:
#     line = line.translate(None, string.punctuation)
#     l = line.split()
#     for x in l:
#         dic[x] = dic.get(x, 0) + 1
# # tmp = []
# # for k, v in dic.items():
# #     tmp.append((v, k))
# # tmp.sort(reverse=True)
# #
# # for v, k in tmp[:10]:
# #     print k, v
#
# # to make it shorter
# tmp = [(v, k) for (k, v) in dic.items()]
# tmp.sort(reverse=True)
# for v, k in tmp[:10]:
#     print k, v


# # print list of words sorted by length, in decreasing order, if same amount of char, sorts in alphabetical order
# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = []
# for word in words:
#     t.append((len(word), word))
# t.sort(reverse=True)
# lst = []
# for l, w in t:
#     lst.append(w)
# print lst


# # Ex. 10.1
#
# fname = raw_input('Enter fine name: ')
# if len(fname) < 1:
#     fname = 'mbox-short.txt'
# fhand = open(fname)
# dic = {}
# lst = []
# for line in fhand:
#     if line.startswith('From '):
#         line = line.split()
#         lst.append(line[1])
# for word in lst:
#     dic[word] = dic.get(word, 0) + 1
# last = sorted([(v, k) for k, v in dic.items()])
# last.sort(reverse=True)
# for v, k in last[:1]:
#     print k, v



# # Ex. 10.2
#
# fname = raw_input('Enter fine name: ')
# if len(fname) < 1:
#     fname = 'mbox-short.txt'
# fhand = open(fname)
# dic = {}
# lst = []
# for line in fhand:
#     if line.startswith('From '):
#         line = line.split()
#         lst.append(line[5])
# hours = []
# for x in lst:
#     h, m, s = x.split(':')
#     hours.append(h)
# for h in hours:
#     dic[h] = dic.get(h, 0) + 1
# newlst= sorted(dic.items())
# for k, v in newlst:
#     print k, v


# Ex. 10.3
import string
fname = raw_input('Enter file name: ')
fhand = open(fname)
dic = {}
lst = []
for line in fhand:
    line = line.lower()
    nline = line.translate(None, string.punctuation)
    l = nline.split()
    for word in l:
        for x in range(len(word)):
            lst.append(word[x])
for char in lst:
    if not char.isdigit():
        dic[char] = dic.get(char, 0) + 1
slst = []
for k, v in dic.items():
    slst.append((v, k))
slst.sort(reverse=True)
for v, k in slst:
    print k, v





