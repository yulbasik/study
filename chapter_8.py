# Calculate average
# nlist = list()
#
# while True:
#     try:
#         inp = raw_input('Enter a number: ')
#         if inp == 'done': break
#         n = float(inp)
#         nlist.append(n)
#     except:
#         print 'number please: '
# print 'Average: ', sum(nlist)/len(nlist)
# print nlist





# # Ex. 8.1 and 8.2 Functions that return or doesn't return values on lists'
# def chop(s):
#     del s[0]
#     del s[len(s) - 1]
#
# def middle(d):
#     return d[1:len(d) - 1]
#
# t = [1, 5, 7, 6, 8, 3]
#
# print middle(t)
# chop(t)
# print t




# Ex 8.4 Romeo file
# file = raw_input('Enter your file name:')
# try:
#     fhand = open(file)
# except:
#     fhand = open('romeo.txt')
# words = list()
# for line in fhand:
#     line.strip()
#     l = line.split()
#     for i in range(0, len(l)):
#         if not l[i] in words:
#             words.append(l[i])
# words.sort()
# print words



# #  Ex. 8.5
# fname = raw_input("Enter file name: ")
# if len(fname) < 1: fname = "mbox-short.txt"
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('From '):
#         l = line.split()
#         count += 1
#         print l[1]
# print 'There were %s lines in the file with From as the first word' % count

# Ex. 8.6

count = []
while True:
    input = raw_input('Enter a number or "done"\n')
    if input == 'done': break
    else:
        try:
            inp = float(input)
            count.append(inp)
        except:
            print 'numbers please'
            continue
print 'Maximum: ', max(count)
print 'Minimum: ', min(count)









