inp = raw_input()
count = 0
for i in inp:
    if i.isupper():
        count += 1
if count > len(inp)/2:
    print inp.upper()
else:
    print inp.lower()
