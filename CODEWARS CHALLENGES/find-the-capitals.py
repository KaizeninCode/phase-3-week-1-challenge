# CHALLENGE LINK https://www.codewars.com/kata/find-the-capitals
def capital(capitals): 
    return [f"The capital of {item['state'] if 'state' in item else item['country']} is {item['capital'].capitalize()}" for item in capitals if 'state' in item or 'country' in item]