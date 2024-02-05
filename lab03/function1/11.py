def palindrome(s):
    if s != s[::-1]:
        print("It's not Palindrome!")
    else:
        print("It's Palindrome!")

s = input()
palindrome(s)