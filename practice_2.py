sm = 0
lr = 0


def largest(n):
    numb = None
    if numb is None or numb < n:
        numb = n
    return numb


def smallest(n):
    small = None
    if small is None or small > n:
        small = n
        return small

while True:
    int = raw_input('enter number:')
    if int == 'done':
        print'Done!'
        break
    else:
         try:
             n = float(int)
             lr = largest(n)
             sm = smallest(n)
         except:
             print 'invalid'
print 'Largest:', lr, 'Smallest:', sm
