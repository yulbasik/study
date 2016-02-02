inp = raw_input()
s = inp.replace('WUB', ' ', len(inp))
# import re
# i = re.sub(' +', ' ', n)
new = s.split()
string = ' '.join(str(x) for x in new)
print string





