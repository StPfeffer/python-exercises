import re


x = 'My 2 favorite numbers are 19 and 42.'
y = re.findall('[0-9]+', x) # one or more (+) digits
print(y) # ['2', '19', '42']

y = re.findall('[AEIOU]+', x)
print(y) # []