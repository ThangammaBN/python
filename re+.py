import re
Regex = re.compile(r'Bat(wo)+man')
mo = Regex.search('Batwowoman')
print(mo.group())