import re

string = 'asdasdasdasd%$89'
password = re.compile(r'[\w$%@#]{7,}\d$')
check = password.fullmatch(string)
print(check)