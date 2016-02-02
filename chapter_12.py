# import urllib
# import re
# inp = raw_input('your URL: ')
# html = urllib.urlopen(inp).read()
# lst = re.findall('href="(http://.+?)"', html)
# for x in lst:
#     print x

# /////////////////////////////////////////////////////////////////////
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print data
# mysock.close()

# import urllib
# fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
#     print line.strip()

# /////////////////////////////////////////////////////////
# import urllib
# from BeautifulSoup import *
# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print tag.get('href', None)
#     print type(tag)
#     print type(tags)

# //////////////////////////////////////////////////

# import urllib
# img = urllib.urlopen('http://www.py4inf.com/cover.jpg').read()
# fhand = open('cover.jpg', 'w')
# fhand.write(img)
# fhand.close()

# ////////////////////////////////////////////////

# # Ex. 12.1-2
#
# import socket
#
# inp = raw_input('Enter url: ')
# host = inp.split('/')[2]
#
# print host
# try:
#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mysock.connect((host, 80))
#     mysock.send('GET ' + inp + 'HTTP/1.0\n\n')
#     count = 0
#     x = ''
#     while True:
#         data = mysock.recv(512)
#         if (len(data) < 1): break
#         count += len(data)
#         x += data
#     print x[:3000]
#     print count
#     mysock.close()
# except:
#     print 'invalid url, closing the programm'

# //////////////////////////////////////////////////////////////

# Ex. 12.3

# import urllib
# inp = raw_input('Enter URL: ')
# file = urllib.urlopen(inp).read()
# count = 0
# x = ''
# for line in file:
#     count += len(line)
#     x += line
# print x[:3000]
# print count

# ////////////////////////////////////
# 1 assignment

# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
# x = ''
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     x += data
# lst = x.split('\r\n\r\n')
# print lst[0]
# mysock.close()

# //////////////////////////////////////////////
# Ex. 12.4

# import urllib
# from BeautifulSoup import *
#
# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
#
#
# tags = soup('p')
# print len(tags)
# print tags

# ///////////////////////////////////////////////////////

# Assignment 2

# import urllib
# from BeautifulSoup import *
#
# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()
#
# soup = BeautifulSoup(html)
# count = 0
# lst = []
# num = []
# # Retrieve all of the anchor tags
# tags = soup('span')
# for tag in tags:
#     lst.append(tag.contents[0])
#     count += 1
# for x in lst:
#     num.append(int(x))
# print 'Count: ' + `count`
# print 'Sum: ' + `sum(num)`


# ////////////////////////////////////////////////////////////////
#  Assignment 3

import urllib
from BeautifulSoup import*
import re
url = raw_input('Enter - ')
count = int(raw_input('enter count: '))
pos = int(raw_input('Enter position: '))
mycount = 0
while True:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    lst = []
    for tag in tags:
        n = tag.get('href', None)
        lst.append(n)
    url = lst[pos - 1]
    mycount += 1
    if mycount == count:
        name = re.findall('by.(.\S+)[.]html$', lst[pos - 1])
        print name[0]
        break





