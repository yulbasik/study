inp = raw_input()
sinp = raw_input()
f = inp.lower()
s = sinp.lower()
def funccia(f, s):
    for i in range(0, len(f)):
        if f[i] > s[i]:
            return '1'
        if f[i] < s[i]:
            return '-1'
    return '0'
print funccia(f, s)
