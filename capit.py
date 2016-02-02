# the right solution for problem with Petia 112A
# def comp(f, s):
#     for i in range(0, len(f)):
#         fi = f[i]
#         si = s[i]
#         if fi < si:
#             return -1
#         elif fi > si:
#             return 1
#     return 0
#---------------------------------------------------------------

#     alp = 'abcdefghijklmnopqrstuvwxyz'
#     for letter in f:
#         letter = alp.find(letter, 0)
#         for let in s:
#             let = alp.find(let, 0)
#             if letter < let:
#                 return -1
#             elif letter == let:
#                 continue
#             else:
#                 return 1
#     return 0
#
# inp = raw_input()
# inp_2 = raw_input()
# f = inp.lower()
# s = inp_2.lower()
# print comp(f, s)

def check(xs, ys):
    for i in range(0, len(xs)):
        v = xs[i]
        for s in range(0, len(ys)):
            if v == ys[s]:
                return 'yes'
    return 'no'



xs = [1, 6, 3, 9, 9]
ys = [5, 0, 4, 5, 7]
print check(xs, ys)
