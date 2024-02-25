import re
txt = input()
p = re.compile("(?=[A-Z])")
print(p.sub(' ', txt))