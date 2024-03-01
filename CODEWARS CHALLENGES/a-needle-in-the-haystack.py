# CHALLENGE LINK https://www.codewars.com/kata/a-needle-in-the-haystack
def find_needle(haystack):
    for i, item in enumerate(haystack):
        if item == 'needle':
            return f'found the needle at position {i}'
    return 'Could not find the needle'