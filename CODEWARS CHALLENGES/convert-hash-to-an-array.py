# CHALLENGE LINK https://www.codewars.com/kata/convert-hash-to-an-array
def convert_hash_to_array(h):
    return sorted([[k, v] for k, v in h.items()])