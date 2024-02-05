def reverse_sentence(s1):
    words = s1.split()
    rev_word = reversed(words)

    rev_sentence = ' '.join(rev_word)
    return rev_sentence

s1 = input()
result = reverse_sentence(s1)
print(result)