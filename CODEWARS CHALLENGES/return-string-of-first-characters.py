# CHALLENGE LINK https://www.codewars.com/kata/return-string-of-first-characters
def make_string(s):
    return ''.join(word[0] for word in s.split())