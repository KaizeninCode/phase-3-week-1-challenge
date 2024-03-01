# CHALLENGE LINK https://www.codewars.com/kata/unique-string-characters
def solve(a,b):
    return ''.join(char for char in a if char not in b) + ''.join(char for char in b if char not in a)