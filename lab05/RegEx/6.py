import re
txt = input()
pattern = "[ ,.]"
x = re.sub(pattern, ":" , txt)
print(x)