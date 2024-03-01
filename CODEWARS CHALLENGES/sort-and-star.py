# CHALLENGE LINK https://www.codewars.com/kata/sort-and-star
def two_sort(array):
    array.sort()
    return '***'.join(array[0])
