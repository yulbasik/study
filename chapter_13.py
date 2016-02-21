
# import xml.etree.ElementTree as ET
# data = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>009</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff> '''
#
# tree = ET.fromstring(data)
# lst = tree.findall('users/user')
# print 'User count:', len(lst)
# for item in lst:
#     print 'Name:' , item.find('name').text
#     print 'ID', item.find('id').text
#     print 'Attr:' , item.get('x')

# /////////////////////////////////////////////////////////////////////////
# EX.1 Assignment chapter 13

import urllib
import xml.etree.ElementTree as ET

inp = raw_input('Enter location:')
url = urllib.urlopen(inp).read()
stuff = ET.fromstring(url)
lst = stuff.findall('comments/comment')
count = 0
s = 0
for item in lst:
    count += 1
    s += int(item.find('count').text)
print 'Retrieving ', inp
print 'Retrieved ', len(url), 'characters'
print 'Count: ', count
print 'Sum: ', s
