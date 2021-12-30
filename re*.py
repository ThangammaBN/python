import re
Regex = re.compile(r'Bat(wo)*man')
mo = Regex.search('Batwoman')
print(mo.group())
