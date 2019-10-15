import re

code = 'public void aMethod(){ System.out.println(); }'

codeblock = re.compile(r'\{(.*?)\}')

search = codeblock.search(code)

print(search.group())


code = 'public void aMethod(){ System.out.println(); }'
match = re.search(r'{(.*?)}', code)
print(match.group())
