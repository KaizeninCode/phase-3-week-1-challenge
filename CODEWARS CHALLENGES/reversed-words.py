# CHALLENGE LINK https://www.codewars.com/kata/reversed-words
def reverse_words(s):
    string_list = s.split(" ")
    reversed_list = string_list[::-1]
    reversed_string = " ".join(reversed_list)
    return reversed_string