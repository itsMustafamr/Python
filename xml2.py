import xml.etree.ElementTree as ET
#here users is the parents and each user is the children.
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
      <age>69</age>
    </user>           
    <user x="7">
      <id>009</id>
      <age>28</age>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
    print('age', item.find('age').text)