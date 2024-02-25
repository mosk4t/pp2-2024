import re
txt = input()
p = re.compile("(?=[A-Z])")
print(p.sub('_', txt).lower())