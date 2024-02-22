import re

string1 = '123(23)'
string2 = '1234'

re_format = re.compile('\(([^)]+)')

print(re_format.match(string1))
print(re_format.match(string2))