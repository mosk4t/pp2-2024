from itertools import permutations 
def string_permutation(s):
    if len(s) == 1:
        return s
    perm_s = permutations(s)
    for i in list(perm_s):
        print(''.join(i))
s = input()
string_permutation(s)