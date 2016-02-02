def f(s):
    if len(s) > 10:
        last = len(s)-1
        length = s[1: last]
        numb = len(length)
        abbr = s[0] + '%s' % numb + s[len(s)-1]
        return abbr
    else:
        return s

n = int(raw_input())
for i in range(0, n):
  line = raw_input()
  new_line = f(line)
  print new_line





