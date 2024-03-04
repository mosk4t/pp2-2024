s = input()
upp = sum(map(lambda a : a.isupper(), s))
low = sum(map(lambda a : a.islower(), s))
print(f"Upper case letters: {upp} \nLower case letters: {low}")
