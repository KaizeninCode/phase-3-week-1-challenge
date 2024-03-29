# CHALLENGE LINK https://www.codewars.com/kata/the-first-non-repeated-character-in-a-string
def first_non_repeated(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count == 1:
            return char
    return None