# CHALLENGE LINK https://www.codewars.com/kata/vowel-remover
def shortcut(s):
    vowels = 'aeiou'
    return ''.join(char for char in s if char not in vowels)