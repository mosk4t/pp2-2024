s = input()
s1 = "".join(reversed(s))
if s == s1:
    print("YES")
else:
    print("NO")