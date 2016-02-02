# # ex. 11.1
# import re
# inp = raw_input('Enter your reg expression: ')
# hand = open('mbox.txt')
# count = 0
# for line in hand:
#     line = line.strip()
#     ex = re.findall(inp, line)
#     if len(ex) > 0:
#         count += len(ex)
# print 'The mbox.txt file had %d lines that matched %s' % (count, inp)

# # Ex 11.2
# import re
# inp = raw_input('Enter file name: ')
# hand = open(inp)
# lst = []
# aver = []
# for line in hand:
#     line = line.strip()
#     x = re.findall('^New Revision:.\s*([0-9.]+)', line)
#     if len(x) > 0:
#         for s in x:
#             lst.append(s)
# for n in lst:
#     aver.append(float(n))
# print sum(aver) / len(aver)


# # Assignment
# import re
# inp = raw_input('Enter file name: ')
# hand = open(inp)
# lst = []
# for line in hand:
#     line = line.strip()
#     x = re.findall('[0-9]+', line)
#     if len(x) > 0:
#         for n in x:
#             lst.append(int(n))
# print sum(lst)


# the same through the list comprehension
import re
print sum( [ int(x) for x in re.findall('[0-9]+', open('regex_sum_42.txt').read()) ] )