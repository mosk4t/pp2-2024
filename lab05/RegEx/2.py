import re
txt = input()
x = re.search("a{1}b{2,3}", txt)
print(x)