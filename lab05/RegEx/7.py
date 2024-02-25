import re
txt = input()
p = re.compile("_([a-z])")
print(p.sub(lambda match: match.group(1).upper(), txt))